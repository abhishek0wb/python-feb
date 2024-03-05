from pymongo import MongoClient 

client = MongoClient("mongodb+srv://youtubepy:ramramlaoo@cluster0.yysgzty.mongodb.net/")

print(client)
db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_video():
    for video in video_collection.find():
        print(f"ID:{video['_id']}, Name:{video ['name']} and Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id': video_id},
        {"$set": {"name":name, "time": time}}
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})



def main():
    while True:
        print("\n Youtube MAnager App")
        print("1. List the video")
        print("2. App the video")
        print("3. Update the video")
        print("4. Delete the video")
        print("5. Exit")
        choice = input("Enter the choice:  ")


        if choice =='1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to updated: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video duration: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id =input("Enter the video ID to delete")
            delete_video(video_id)
        elif choice == '5':
            break        




if __name__ == "__main__":
    main()
