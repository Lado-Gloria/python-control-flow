def hello(*names):
    for name in names:
        print(f"Hello {name}")

def numm(*number):
    ans =0
    for num in number:
      ans += num
      return num          
    # write a functon that accept any integers 
    # and return the result multiply all of them
def data(*datas):
    answer =1
    for dat in datas:
     answer*= dat
    return answer
# define a function with one parameter but
#  prepend two asterisks to the peremeter name.
# (converted into a dictionary)

def student_attributes(**kwangs):
    for key, value in kwangs.items():
       print(f"{key}:{value}")

    #  defualt argument
def my_country(country ="Burundi"):
     print(f"Hello from {country}") 

# A function named concatenate_args that
#  takes any number of string arguments 
# in positional arguments format and 
# concatenates them into a single string
def concate(*names):
    stringtwo =""
    for nam in names:
        stringtwo+=nam

    print(stringtwo)  

# A function named concatenate_kwargs that takes
#  any number of string arguments in keyword arguments
#   format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    return ' '.join(kwargs.values())   
    
    
