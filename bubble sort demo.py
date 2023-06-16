import random

def bubble_sort(data_list):
    number_of_items = len(data_list)
    for i in range(number_of_items):
        for j in range (number_of_items - 1):
            if (data_list [j+1]>data_list[j]):
                holder = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1]=holder
    return data_list    
#create list
#loop through the list to visit each item
#loop thorough list to compare itens to adjacent items in list
#compare adjacenent items in list
#if right element is less than left element then swap positions

def main():
    my_list = [5,7,8,10]
    integer_list = random.sample(range(0, 1000),100)
    sorted_list = bubble_sort(integer_list)
    print(sorted_list)

main()