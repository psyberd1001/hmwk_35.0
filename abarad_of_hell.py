import threading
import multiprocessing
import time

def read_info(file_name):
    all_data = []
    start_time = time.time()
    with open(file_name, 'r') as f_1:
        for line in f_1:
            line.strip()
            all_data.append(line)
    end_time = time.time()
    result_time = end_time - start_time
    print(result_time)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])

if __name__ =='__main__':

    process1 = multiprocessing.Process(target=read_info, args=(filenames[0],))
    process2 = multiprocessing.Process(target=read_info, args=(filenames[1],))
    process3 = multiprocessing.Process(target=read_info, args=(filenames[2],))
    process4 = multiprocessing.Process(target=read_info, args=(filenames[3],))
    process1.start()
    process2.start()
    process3.start()
    process4.start()
