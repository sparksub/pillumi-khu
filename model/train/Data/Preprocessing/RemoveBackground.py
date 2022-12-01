# 알약 이미지 배경 제거 코드
# backgroundremover 라이브러리를 커맨드에서 실행
# 라이브러리 출처: https://github.com/nadermx/backgroundremover

import os
import glob
import os.path as path
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

input_path = "../raw"
output_path = "../remove_background"
file_path_list = glob.glob(path.join(input_path, '*.png'))

for each in file_path_list:
    command = f'backgroundremover -i {each} -o {output_path}/rmbg_{each[-9:]}'
    command = 'backgroundremover -i 22115.png -o rmbg_22115.png'
    os.system(command)