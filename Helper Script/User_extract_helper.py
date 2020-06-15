import pandas 

FILE_PATH = [r'PATH OF RESULT CSV OF WEIBO-SEARCH']
SAVE_PATH = r'SAVE PATH OF USER ID'

def user_extracter(file_path, save_path):
    list_user =  set()
    for path in file_path:
        df = pandas.read_csv(path)
        df_user = df['user_id'].drop_duplicates()
        list_user.update(df_user.values.tolist())
    print(list_user)
    file = open(save_path, 'w')
    for user_id in list_user:
        file.write(str(user_id) + '\n')

if __name__ == '__main__':
    user_extracter(FILE_PATH, SAVE_PATH) 