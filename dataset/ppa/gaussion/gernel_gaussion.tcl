proc test_gaussion {mul1 mul2 mul3 mul4 mul5 mul6 mul7 mul8 mul9 add1 add2 add3 add4 add5 add6 add7 add8 } {
    # a new environment
    remove_design -all
    # some paths
    set report_ppa "/home/liucheng/zhangqing/work_ic/dc/syn/report/deepapprox/node_gaussion_10w"
    set module_path "/home/liucheng/zhangqing/work_ic/dc/rtl/lib"
    set operation_path "/home/liucheng/zhangqing/work_ic/dc/rtl/operation"
    # read approximate circuit library
    set lib_mul8 [glob $module_path/mul8/*.v]
    set lib_add16 [glob $module_path/add16u/*.v]
    set lib_module [glob $module_path/module/*.v]

    # Open file for warning output
    set warning_file [open "warning.txt" w]

    foreach unit_mul8 $lib_mul8 {
        redirect $warning_file {
            analyze -format verilog $unit_mul8
        }
    }
    foreach unit_add16 $lib_add16 {
        redirect $warning_file {
            analyze -format verilog $unit_add16
        }
    }
    # read necessary modules
    redirect $warning_file {
    	analyze -format verilog $module_path/module/unsigned_add16.v
    	analyze -format verilog $module_path/module/unsigned_mul8.v
    }
    # test
    # read design (e.g., sobel)
    redirect $warning_file {
    	analyze -format verilog $operation_path/gernel_gaussion.v
    }

    # print the result
    puts "***********************"
    puts "value: $mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8"

    # choose approximate circuits from 0~30+1
    redirect $warning_file {
    	elaborate gernel_gaussion -parameters "mul81=$mul1,mul82=$mul2,mul83=$mul3,mul84=$mul4,mul85=$mul5,mul86=$mul6,mul87=$mul7,mul88=$mul8,mul89=$mul9,add161=$add1,add162=$add2,add163=$add3,add164=$add4,add165=$add5,add166=$add6,add167=$add7,add168=$add8"
    }
    set_max_delay 2.5 -from [all_inputs] -to [all_outputs] 
    set_min_delay 0.5 -from [all_inputs] -to [all_outputs] 
    #current_design gernel_gaussion
    # dc
    redirect $warning_file {
    	check_design
    	link
    	compile
    }

    # close warning file
    close $warning_file

    # some reports
    report_area > $report_ppa/area/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_power > $report_ppa/power/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    #report_timing
    report_timing -from [all_inputs] -to unsigned_mul81/O > $report_ppa/latency/mul81/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul82/O > $report_ppa/latency/mul82/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul83/O > $report_ppa/latency/mul83/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul84/O > $report_ppa/latency/mul84/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul85/O > $report_ppa/latency/mul85/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul86/O > $report_ppa/latency/mul86/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul87/O > $report_ppa/latency/mul87/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul88/O > $report_ppa/latency/mul88/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_mul89/O > $report_ppa/latency/mul89/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt


    report_timing -from [all_inputs] -to unsigned_add161/O > $report_ppa/latency/add161/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_add162/O > $report_ppa/latency/add162/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_add163/O > $report_ppa/latency/add163/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_add164/O > $report_ppa/latency/add164/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_add165/O > $report_ppa/latency/add165/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_add166/O > $report_ppa/latency/add166/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt 
    report_timing -from [all_inputs] -to unsigned_add167/O > $report_ppa/latency/add167/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing -from [all_inputs] -to unsigned_add168/O > $report_ppa/latency/add168/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt
    report_timing  > $report_ppa/latency/all/$mul1+$mul2+$mul3+$mul4+$mul5+$mul6+$mul7+$mul8+$mul9+$add1+$add2+$add3+$add4+$add5+$add6+$add7+$add8.txt




}
