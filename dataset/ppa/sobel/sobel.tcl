proc test_sobel {add8_1 add8_2 add12_1 add12_2 sub10} {
    # a new environment
    remove_design -all
    # some paths
    set report_ppa "/home/liucheng/zhangqing/work_ic/dc/syn/report/deepapprox/sobel_4w/"
    set module_path "/home/liucheng/zhangqing/work_ic/dc/rtl/lib/"
    set operation_path "/home/liucheng/zhangqing/work_ic/dc/rtl/operation/"
    # read approximate circuit library
    set lib_add8 [glob $module_path/add8/*.v]
    set lib_add12 [glob $module_path/add12/*.v]
    set lib_sub10 [glob $module_path/sub10/*.v]
    set lib_module [glob $module_path/module/*.v]

    # Open file for warning output
    set warning_file [open "warning.txt" w]

    foreach unit_add8 $lib_add8 {
        redirect $warning_file {
            analyze -format verilog $unit_add8
       }
    }
    foreach unit_add12 $lib_add12 {
       redirect $warning_file {
            analyze -format verilog $unit_add12
       }
    }
    foreach unit_sub10 $lib_sub10 {
        redirect $warning_file {
            analyze -format verilog $unit_sub10
        }
    }
    # read necessary modules
    redirect $warning_file {
    	analyze -format verilog $module_path/module/unsigned_add8.v
   	analyze -format verilog $module_path/module/unsigned_add12.v
   	analyze -format verilog $module_path/module/unsigned_sub10.v
    }
    # test
    # read design (e.g., sobel)
    redirect $warning_file {
    	analyze -format verilog $operation_path/sobel.v
    }

    # print the result
    puts "***********************"
    puts "value: $add8_1 $add8_2 $add12_1 $add12_2 $sub10"

    # choose approximate circuits from 0~30+1
    redirect $warning_file {
    	elaborate sobel -parameters "idx1=$add8_1,idx2=$add8_2,idx3=$add12_1,idx4=$add12_2,idx5=$sub10"
    }
    create_clock -period 100 -name virtual_clock
    # dc
    redirect $warning_file {
    	check_design
    	link
    	compile
    }

    # close warning file
    close $warning_file

    # some reports
    report_area > $report_ppa/area/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    report_power > $report_ppa/power/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    report_timing -delay max > $report_ppa/latency/all/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    #report_timing_part
    report_timing -from [all_inputs] -to unsigned_add8_1/O > $report_ppa/latency/add81/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    report_timing -from [all_inputs] -to unsigned_add8_2/O > $report_ppa/latency/add82/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    report_timing -from [all_inputs] -to unsigned_add12_1/O > $report_ppa/latency/add121/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    report_timing -from [all_inputs] -to unsigned_add12_2/O > $report_ppa/latency/add122/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
    report_timing -from [all_inputs] -to unsigned_sub10/O > $report_ppa/latency/sub10/$add8_1+$add8_2+$add12_1+$add12_2+$sub10.txt
}

