source /home/liucheng/zhangqing/work_ic/dc/syn/script/sobel/sobel.tcl
set file [open "/home/liucheng/zhangqing/work_ic/dc/dataset/deepapprox/sobel/dataset_sobel1.txt" r]
set content [read $file]

set add8_lib [dict create "add8u_0E2" 1 "add8u_0JM" 2 "add8u_00M" 3 "add8u_0NH" 4 "add8u_0NQ" 5  "add8u_0NS" 6  "add8u_0PA" 7  "add8u_0PL" 8 "add8u_0TP" 9 "add8u_1HG" 10 "add8u_02Y" 11 "add8u_2AM" 12 "add8u_2J3" 13 "add8u_2LL" 14 "add8u_3RE" 15 "add8u_4M7" 16 "add8u_05G" 17 "add8u_6FT" 18 "add8u_6K6" 19 "add8u_6LG" 20 "add8u_6MZ" 21 "add8u_6P8" 22 "add8u_6PT" 23 "add8u_6QU" 24 "add8u_6R6" 25 "add8u_6S4" 26 "add8u_6SM" 27 "add8u_6TH" 28 "add8u_108" 29 "add8u_0D0" 30 "add8u_0UK" 31 ]
set add12_lib [dict create "add12u_0AF" 1 "add12u_0AZ" 2 "add12u_0B6" 3 "add12u_0C9" 4 "add12u_0G8" 5 "add12u_0JK" 6 "add12u_0LN" 7 "add12u_0PX" 8 "add12u_0UZ" 9 "add12u_0Z5" 10 "add12u_0ZP" 11 "add12u_2KC" 12 "add12u_2L1" 13 "add12u_2UF" 14 "add12u_2UH" 15 "add12u_3K3" 16 "add12u_3L3" 17 "add12u_3R0" 18 "add12u_3UT" 19 "add12u_4NT" 20 "add12u_4TF" 21 "add12u_06R" 22 "add12u_22J" 23 "add12u_28B" 24 "add12u_38J" 25 "add12u_39N" 26 "add12u_50U" 27 "add12u_103" 28 "add12u_187" 29]
set sub10_lib [dict create "sub10_1" 1 "sub10_5" 2 "sub10_6" 3 "sub10_15" 4 "sub10_26" 5 "sub10_65" 6 "sub10_85" 7 "sub10_90" 8 "sub10_130" 9 "sub10_135" 10 "sub10_200" 11 "sub10_210" 12 "sub10_260" 13 "sub10_270" 14]

set lines [split $content "\n"]
foreach line $lines {
    puts "$line"
    set strings [split $line " "]
    lassign $strings add81_value add82_value add121_value add122_value sub10_value
    puts "$add81_value"
    set add81_key [dict get $add8_lib $add81_value]
    set add82_key [dict get $add8_lib $add82_value] 
    set add121_key [dict get $add12_lib $add121_value]
    set add122_key [dict get $add12_lib $add122_value] 
    set sub10_key [dict get $sub10_lib $sub10_value]  
    puts "$add81_key $add82_key $add121_key $add122_key $sub10_key"
    test_sobel $add81_key $add82_key $add121_key $add122_key $sub10_key

}

                

