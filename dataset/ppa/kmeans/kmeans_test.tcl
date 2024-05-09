proc kmeans_core {sub10_1 sub10_2 sub10_3 mul8_1 mul8_2 mul8_3 add16_1 sqrt1 sub10_4 sub10_5 sub10_6  mul8_4 mul8_5 mul8_6  add16_2  sqrt2 } {
remove_design -all
#some parameters
set design_path "/home/liucheng/zhangqing/work_ic/dc/rtl/kmean/"
set report_ppa_path "/home/liucheng/zhangqing/work_ic/dc/syn/report/kmeans/"
set design_name $sub10_1+$sub10_2+$sub10_3+$mul8_1+$mul8_2+$mul8_3+$add16_1+$sqrt1+$sub10_4+$sub10_5+$sub10_6+$mul8_4+$mul8_5+$mul8_6+$add16_2+$sqrt2
#read verilog
set add16u_lib [glob $design_path/uint_lib/add16u/*.v]
set mul8_lib [glob $design_path/uint_lib/mul8/*.v]
set mul11_lib [glob $design_path/uint_lib/mul11/*.v]
set sub10_lib [glob $design_path/uint_lib/sub10/*.v]
set module_lib [glob $design_path/module/*.v]
set core_lib [glob $design_path/core/*.v]

foreach single $add16u_lib {analyze -format verilog $single}
foreach single $mul8_lib {analyze -format verilog $single}
foreach single $mul11_lib {analyze -format verilog $single}
foreach single $sub10_lib {analyze -format verilog $single}
foreach single $module_lib {analyze -format verilog $single}
foreach single $core_lib {analyze -format verilog $single}
#compile design
elaborate kmeans -parameters "sub81=$sub10_1,sub82=$sub10_2,sub83=$sub10_3,mul81=$mul8_1,mul82=$mul8_2,mul83=$mul8_3,add161=$add16_1,sqrt1=$sqrt1,sub84=$sub10_4,sub85=$sub10_5,sub86=$sub10_6,mul84=$mul8_4,mul85=$mul8_5,mul86=$mul8_6,add162=$add16_2,sqrt2=$sqrt2"
#elaborate kmeans
link
compile
#report kmeans ppa

report_area > $report_ppa_path/area/$design_name.txt
report_power > $report_ppa_path/power/$design_name.txt
report_timing -from compute_top/pix -to compute_top/all_distance > $report_ppa_path/latency/all_latency/$design_name.txt
#report single opt ppa
#core1
report_timing -from compute_top/compute_core1/unsigned_sub10_1/A -to compute_top/compute_core1/unsigned_sub10_1/O > $report_ppa_path/latency/core1_latency/sub10_1/$design_name.txt
report_timing -from compute_top/compute_core1/unsigned_sub10_2/A -to compute_top/compute_core1/unsigned_sub10_2/O > $report_ppa_path/latency/core1_latency/sub10_2/$design_name.txt
report_timing -from compute_top/compute_core1/unsigned_sub10_3/A -to compute_top/compute_core1/unsigned_sub10_3/O > $report_ppa_path/latency/core1_latency/sub10_3/$design_name.txt
report_timing -from compute_top/compute_core1/unsigned_mul8_1/A -to compute_top/compute_core1/unsigned_mul8_1/O > $report_ppa_path/latency/core1_latency/mul8_1/$design_name.txt
report_timing -from compute_top/compute_core1/unsigned_mul8_2/A -to compute_top/compute_core1/unsigned_mul8_2/O > $report_ppa_path/latency/core1_latency/mul8_2/$design_name.txt
report_timing -from compute_top/compute_core1/unsigned_mul8_3/A -to compute_top/compute_core1/unsigned_mul8_3/O > $report_ppa_path/latency/core1_latency/mul8_3/$design_name.txt
report_timing -from compute_top/compute_core1/unsigned_add16_1/A -to compute_top/compute_core1/unsigned_add16_1/O > $report_ppa_path/latency/core1_latency/add16_1/$design_name.txt
report_timing -from compute_top/compute_core1/sqrt1/input_data -to compute_top/compute_core1/sqrt1/output_data > $report_ppa_path/latency/core1_latency/sqrt/$design_name.txt
#core2
report_timing -from compute_top/compute_core2/unsigned_sub10_1/A -to compute_top/compute_core2/unsigned_sub10_1/O > $report_ppa_path/latency/core2_latency/sub10_1/$design_name.txt
report_timing -from compute_top/compute_core2/unsigned_sub10_2/A -to compute_top/compute_core2/unsigned_sub10_2/O > $report_ppa_path/latency/core2_latency/sub10_2/$design_name.txt
report_timing -from compute_top/compute_core2/unsigned_sub10_3/A -to compute_top/compute_core2/unsigned_sub10_3/O > $report_ppa_path/latency/core2_latency/sub10_3/$design_name.txt
report_timing -from compute_top/compute_core2/unsigned_mul8_1/A -to compute_top/compute_core2/unsigned_mul8_1/O > $report_ppa_path/latency/core2_latency/mul8_1/$design_name.txt
report_timing -from compute_top/compute_core2/unsigned_mul8_2/A -to compute_top/compute_core2/unsigned_mul8_2/O > $report_ppa_path/latency/core2_latency/mul8_2/$design_name.txt
report_timing -from compute_top/compute_core2/unsigned_mul8_3/A -to compute_top/compute_core2/unsigned_mul8_3/O > $report_ppa_path/latency/core2_latency/mul8_3/$design_name.txt
report_timing -from compute_top/compute_core2/unsigned_add16_1/A -to compute_top/compute_core2/unsigned_add16_1/O > $report_ppa_path/latency/core2_latency/add16_1/$design_name.txt
report_timing -from compute_top/compute_core2/sqrt1/input_data -to compute_top/compute_core2/sqrt1/output_data > $report_ppa_path/latency/core2_latency/sqrt/$design_name.txt

}

