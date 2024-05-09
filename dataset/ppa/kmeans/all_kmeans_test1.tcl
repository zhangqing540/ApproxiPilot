source /home/liucheng/zhangqing/work_ic/dc/syn/script/kmeans/kmeans_test.tcl
set file [open "/home/liucheng/zhangqing/work_ic/dc/dataset/kmeans/dataset1.txt" r]
set content [read $file]
set add16_lib [dict create "add16u_0BC" 1  "add16u_0CB" 2 "add16u_0EZ" 3 "add16u_0GN" 4 "add16u_0GX" 5 "add16u_0HE" 6 "add16u_0HK" 7 "add16u_0J3" 8 "add16u_0K3" 9 "add16u_0KG" 10 "add16u_0KU" 11 "add16u_0NL" 12 "add16u_0NT" 13 "add16u_0P8" 14 "add16u_0PT" 15 "add16u_0RH" 16 "add16u_0RJ" 17 "add16u_0SD" 18 "add16u_0SL" 19 "add16u_0TA" 20 "add16u_0U8" 21 "add16u_0UV" 22 "add16u_0VA" 23 "add16u_1A5" 24 "add16u_07T" 25 "add16u_08V" 26 "add16u_15Q" 27 "add16u_067" 28 "add16u_110" 29 "add16u_126" 30 "add16u_162" 31]
set mul8_lib [dict create  "mul8u_1A0M" 1 "mul8u_1DMU" 2 "mul8u_1JJQ" 3 "mul8u_1SX" 4 "mul8u_2NDH" 5 "mul8u_2V0" 6 "mul8u_4TF" 7 "mul8u_4X5" 8 "mul8u_8U3" 9 "mul8u_12KA" 10 "mul8u_12YX" 11 "mul8u_17C8" 12 "mul8u_17MJ" 13 "mul8u_17MN" 14 "mul8u_17R6" 15 "mul8u_18UH" 16 "mul8u_19XF" 17 "mul8u_27Y" 18 "mul8u_197B" 19 "mul8u_874" 20 "mul8u_BG1" 21 "mul8u_C67" 22 "mul8u_DG8" 23 "mul8u_GJM" 24 "mul8u_GTR" 25 "mul8u_L93" 26 "mul8u_LK8" 27 "mul8u_NLX" 28 "mul8u_R36" 29 "mul8u_R92" 30 "mul8u_T83" 31 "mul8u_TD3" 32 "mul8u_XFM" 33 "mul8u_Z9D" 34 "mul8u_ZB3" 35 "mul8u_ZDF" 36 "mul8u_0AB" 0]
set sub10_lib [dict create "sub10_1" 1 "sub10_5" 2 "sub10_6" 3 "sub10_15" 4 "sub10_26" 5 "sub10_65" 6 "sub10_85" 7 "sub10_90" 8 "sub10_130" 9 "sub10_135" 10 "sub10_200" 11 "sub10_210" 12 "sub10_260" 13 "sub10_270" 14]
set sqrt_lib [dict create "mul11u_00K" 1 "mul11u_00H" 0 "mul11u_01Z" 2 "mul11u_003" 3 "mul11u_03N" 4 "mul11u_05D" 5 "mul11u_09Z" 6 "mul11u_024" 7 "mul11u_041" 8 "mul11u_067" 9 "mul11u_097" 10]
set sqrt_lib
set lines [split $content "\n"]
foreach line $lines {
    puts "$line"
    set strings [split $line " "]
    lassign $strings sub101_value sub102_value sub103_value mul81_value mul82_value mul83_value add161_value sqrt1_value sub104_value sub105_value sub106_value mul84_value mul85_value mul86_value add162_value sqrt2_value

    set sub101_key [dict get $sub10_lib $sub101_value]
    set sub102_key [dict get $sub10_lib $sub102_value] 
    set sub103_key [dict get $sub10_lib $sub103_value]
    set mul81_key [dict get $mul8_lib $mul81_value] 
    set mul82_key [dict get $mul8_lib $mul82_value] 
    set mul83_key [dict get $mul8_lib $mul83_value]
    set add161_key [dict get $add16_lib $add161_value] 
    set sqrt1_key [dict get $sqrt_lib $sqrt1_value]
    set sub104_key [dict get $sub10_lib $sub104_value]  
    set sub105_key [dict get $sub10_lib $sub105_value]  
    set sub106_key [dict get $sub10_lib $sub106_value]  
    set mul84_key [dict get $mul8_lib $mul84_value]  
    set mul85_key [dict get $mul8_lib $mul85_value]  
    set mul86_key [dict get $mul8_lib $mul86_value]  
    set add162_key [dict get $add16_lib $add162_value]  
    set sqrt2_key [dict get $sqrt_lib $sqrt2_value]    
    puts "$sub101_key $sub102_key $sub103_key $mul81_key $mul82_key $mul83_key $add161_key $sqrt1_key $sub104_key $sub105_key $sub106_key $mul84_key $mul85_key $mul86_key $add162_key $sqrt2_key"
    kmeans_core $sub101_key $sub102_key $sub103_key $mul81_key $mul82_key $mul83_key $add161_key $sqrt1_key $sub104_key $sub105_key $sub106_key $mul84_key $mul85_key $mul86_key $add162_key $sqrt2_key 
}

