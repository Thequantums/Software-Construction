There are many issues  i've encountered doing the homework 6. First of all, which section of the code in main function to multi-threaded. I realized to muti-thread the loop with each thread as one px and increment. But then if the width and the number of threads arent equal, we cant create each thread as each pixel. So,each thread start the px with its own index up to width to guarantee cover the range. Second, how to get scaled_color output for each thread and printf in main. I was to create a structure contained arrcolor for scaled_color output and index. But since i used the above method to multi-thread, i cant simply write a arrcolor[x][y][i] to print in main because each thread has its own arrcolor. So, i declared it as a global variable to be shared by all threads with its different starting index. The casting of void* to int resulted in an error when i first did because it did num = (int) argp. but the right one is num = *(int*) argp. Then i came to a problem of linking because it didnt include the library "pthread.h". Finnally, i came into a formate error from make clean where i included the new line in wrong loop when output the arrcolor.

Running the make clean check command, i got a time for different number of parallel like follow:

time ./srt 1-test.ppm >1-test.ppm.tmp

real    0m41.289s
user    0m41.279s
sys     0m0.003s
mv 1-test.ppm.tmp 1-test.ppm
time ./srt 2-test.ppm >2-test.ppm.tmp

real    0m21.397s
user    0m42.715s
sys     0m0.001s
mv 2-test.ppm.tmp 2-test.ppm
time ./srt 4-test.ppm >4-test.ppm.tmp

real    0m11.194s
user    0m44.475s
sys     0m0.001s
mv 4-test.ppm.tmp 4-test.ppm
time ./srt 8-test.ppm >8-test.ppm.tmp

real    0m5.761s
user    0m44.643s
sys     0m0.007s
mv 8-test.ppm.tmp 8-test.ppm

As the number of threads increases, the real time is reduced, making the processing of the program faster. with 1 thread is the slowest and 8 threads is the fastest. This is because many threads calculate the scaled-color parallelly. Howevere, as usually, the user time which is the accumulative time spent on cpu is slightly increasing as the number of threads increases because the sum of many thread processing in cpu should be roughtly equal to the time spent on cpu of a single thread program. The sys time doesn't change much. In conclusion, the SRT drastically improves with multiple threaded implementation.


