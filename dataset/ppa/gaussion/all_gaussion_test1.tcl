source /home/liucheng/zhangqing/work_ic/dc/syn/script/gaussion/gernel_gaussion.tcl
set file [open "/home/liucheng/zhangqing/work_ic/dc/dataset/deepapprox/gaussion_10w/dataset1.txt" r]
set content [read $file]

set add16_lib [dict create "add16u_0BC" 1  "add16u_0CB" 2 "add16u_0EZ" 3 "add16u_0GN" 4 "add16u_0GX" 5 "add16u_0HE" 6 "add16u_0HK" 7 "add16u_0J3" 8 "add16u_0K3" 9 "add16u_0KG" 10 "add16u_0KU" 11 "add16u_0NL" 12 "add16u_0NT" 13 "add16u_0P8" 14 "add16u_0PT" 15 "add16u_0RH" 16 "add16u_0RJ" 17 "add16u_0SD" 18 "add16u_0SL" 19 "add16u_0TA" 20 "add16u_0U8" 21 "add16u_0UV" 22 "add16u_0VA" 23 "add16u_1A5" 24 "add16u_07T" 25 "add16u_08V" 26 "add16u_15Q" 27 "add16u_067" 28 "add16u_110" 29 "add16u_126" 30 "add16u_162" 31]
set mul8_lib [dict create "mul8u_0AB" 0 "mul8u_1A0M" 1 "mul8u_1DMU" 2 "mul8u_1JJQ" 3 "mul8u_1SX" 4 "mul8u_2NDH" 5 "mul8u_2V0" 6 "mul8u_4TF" 7 "mul8u_4X5" 8 "mul8u_8U3" 9 "mul8u_12KA" 10 "mul8u_12YX" 11 "mul8u_17C8" 12 "mul8u_17MJ" 13 "mul8u_17MN" 14 "mul8u_17R6" 15 "mul8u_18UH" 16 "mul8u_19XF" 17 "mul8u_27Y" 18 "mul8u_197B" 19 "mul8u_874" 20 "mul8u_BG1" 21 "mul8u_C67" 22 "mul8u_DG8" 23 "mul8u_GJM" 24 "mul8u_GTR" 25 "mul8u_L93" 26 "mul8u_LK8" 27 "mul8u_NLX" 28 "mul8u_R36" 29 "mul8u_R92" 30 "mul8u_T83" 31 "mul8u_TD3" 32 "mul8u_XFM" 33 "mul8u_Z9D" 34 "mul8u_ZB3" 35 "mul8u_ZDF" 36]
set lines [split $content "\n"]
foreach line $lines {
    puts "$line"
    set strings [split $line " "]
    lassign $strings mul81_value mul82_value mul83_value mul84_value mul85_value mul86_value mul87_value mul88_value mul89_value add161_value add162_value add163_value add164_value add165_value add166_value add167_value add168_value

    set mul81_key [dict get $mul8_lib $mul81_value]
    set mul82_key [dict get $mul8_lib $mul82_value] 
    set mul83_key [dict get $mul8_lib $mul83_value]
    set mul84_key [dict get $mul8_lib $mul84_value] 
    set mul85_key [dict get $mul8_lib $mul85_value] 
    set mul86_key [dict get $mul8_lib $mul86_value]
    set mul87_key [dict get $mul8_lib $mul87_value] 
    set mul88_key [dict get $mul8_lib $mul88_value]
    set mul89_key [dict get $mul8_lib $mul89_value]  
    set add161_key [dict get $add16_lib $add161_value]  
    set add162_key [dict get $add16_lib $add162_value]  
    set add163_key [dict get $add16_lib $add163_value]  
    set add164_key [dict get $add16_lib $add164_value]  
    set add165_key [dict get $add16_lib $add165_value]  
    set add166_key [dict get $add16_lib $add166_value]  
    set add167_key [dict get $add16_lib $add167_value]  
    set add168_key [dict get $add16_lib $add168_value]  
    puts "$mul81_key $mul82_key $mul83_key $mul84_key $mul85_key $mul86_key $mul87_key $mul88_key $mul89_key $add161_key $add162_key $add163_key $add164_key $add165_key $add166_key $add167_key $add168_key"
    test_gaussion $mul81_key $mul82_key $mul83_key $mul84_key $mul85_key $mul86_key $mul87_key $mul88_key $mul89_key $add161_key $add162_key $add163_key $add164_key $add165_key $add166_key $add167_key $add168_key
}

                

