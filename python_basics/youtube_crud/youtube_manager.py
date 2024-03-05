import json


def load_data():
    try:
        with open('youtube,txt', 'r') as file:
            test= json.load(file)
            return test

    except FileNotFoundError :
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("enter video name: ")
    time = input("enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)



def update(videos):
   list(videos)
   index = int(input("enter the video to update"))
   if 1<= index <= len(videos):
       name = input("enter video name")
       time = input("enter video time")
       videos[index-1] = {'name' :name, "time": time}
       save_data_helper(videos)
   else:
       print("invaild")
          


def delete(videos):
   list(videos)
   index = int(input("enter the video to delete"))
   if 1 <= index <= len(videos):
       del videos[index-1]
       save_data_helper(videos)
   else:
       print("invaild")    
       
   


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager")
        print("1. List of all the video")
        print("2. Add a video")
        print("3. Update video list")
        print("4. Deletd the video")
        print("5. Exit")
        choice =  input("Enter the choice: ")
        

        match choice:
            case '1':
                list(videos)
            case '2':
                add_video(videos)
            case '3':
                update(videos)
            case '4':
                delete(videos)
            case '5':
                break
            case _:
                print("invaild") 

if __name__ == "__main__":
    main()

