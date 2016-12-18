import numpy
import random

def judge(play_matrix):
	length = len(play_matrix[0])

	new_play_matrix = numpy.zeros((length,length))
	for i in range(length):
		for j in range(length):
			data_list = [];
			if i == 0:
				if j == 0:
					data_list.append(play_matrix[i][j+1])
					data_list.append(play_matrix[i+1][j+1])
					data_list.append(play_matrix[i+1][j])
				elif j==length-1:
					data_list.append(play_matrix[i][j-1])	
					data_list.append(play_matrix[i+1][j-1])
					data_list.append(play_matrix[i+1][j])
				else:
					data_list.append(play_matrix[i][j-1])	
					data_list.append(play_matrix[i][j+1])
					data_list.append(play_matrix[i+1][j])
					data_list.append(play_matrix[i+1][j+1])
					data_list.append(play_matrix[i+1][j-1])

			elif i == length-1:
				if j == 0:
					data_list.append(play_matrix[i-1][j])
					data_list.append(play_matrix[i-1][j+1])
					data_list.append(play_matrix[i][j+1])
				elif j==length-1:
					data_list.append(play_matrix[i][j-1])
					data_list.append(play_matrix[i-1][j-1])
					data_list.append(play_matrix[i-1][j])
				else:	
					data_list.append(play_matrix[i][j-1])	
					data_list.append(play_matrix[i][j+1])
					data_list.append(play_matrix[i-1][j])
					data_list.append(play_matrix[i-1][j-1])
					data_list.append(play_matrix[i-1][j+1])		
			else:
				if j==0:
					data_list.append(play_matrix[i-1][j])	
					data_list.append(play_matrix[i+1][j])
					data_list.append(play_matrix[i][j+1])
					data_list.append(play_matrix[i-1][j+1])
					data_list.append(play_matrix[i+1][j+1])
				elif j == length-1:
					data_list.append(play_matrix[i-1][j])	
					data_list.append(play_matrix[i+1][j])
					data_list.append(play_matrix[i][j-1])
					data_list.append(play_matrix[i-1][j-1])
					data_list.append(play_matrix[i+1][j-1])
				else:
					data_list.append(play_matrix[i-1][j-1])	
					data_list.append(play_matrix[i-1][j])
					data_list.append(play_matrix[i-1][j+1])
					data_list.append(play_matrix[i][j+1])
					data_list.append(play_matrix[i][j-1])
					data_list.append(play_matrix[i+1][j-1])	
					data_list.append(play_matrix[i+1][j])
					data_list.append(play_matrix[i+1][j+1])
			
			count = sum(data_list)
			if count == 3:
				new_play_matrix[i][j] = 1
			elif count == 2:
				new_play_matrix[i][j] = play_matrix[i][j]
			else:
				new_play_matrix[i][j] =0;

	return new_play_matrix;

def sum_count(play_matrix):
	one_count = 0
	for item in play_matrix:
		one_count += sum(item)

	return one_count	

def like_eight_queen():
	
	play_matrix = numpy.zeros((15,15))
	
	length = len(play_matrix[0])

	limit = length**2
	
	for i in range(length):
		for j in range(length):
			play_matrix[i][j] = random.randint(0,99)%2

	print("original is: \n");
	print(play_matrix);		
	count = 1
	one_count = sum_count(play_matrix) 
	origin_matrix = []
	while (one_count!=0)|(one_count!=limit):
		origin_matrix = play_matrix.copy()
		play_matrix = judge(play_matrix);
		print("\nthe result of "+str(count)+"th transform as following:");
		print(play_matrix)
		one_count = sum_count(play_matrix)
		count += 1
		# flag = 0;
		if (origin_matrix==play_matrix).all():
			break 
		elif count>1000:
			break




		# if count >= 3:
		# 	break

if __name__ == '__main__':
	like_eight_queen()


					