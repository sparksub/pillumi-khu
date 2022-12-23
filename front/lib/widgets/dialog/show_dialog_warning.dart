import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;
import 'package:image_picker/image_picker.dart';

ShowDialogWarning(BuildContext context) async {
  return await showDialog(
    context: context,
    builder: (BuildContext context) {
      return  AlertDialog(
        title: Text('사진 등록 시 주의사항!',
          textAlign: TextAlign.center,
          style: TextStyle(
            color: palette.red,
            fontWeight: FontWeight.bold,
            fontSize: 20
          ),
        ),
        elevation: 10,
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8.0)
        ),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            waringText("1. 밝은 조명 아래서 찍어주세요."),
            waringText("2. 알약이 전부 보이게 찍어주세요."),
            waringText("3. 깔끔한 배경에서 찍어주세요."),
            const SizedBox(height: 20),
            waringText("*예시*"),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Column(
                  mainAxisSize: MainAxisSize.min,
                  children: const [
                    Image(
                      image: AssetImage('assets/bad-photo.jpg'),
                      width: 80,
                    ),
                    SizedBox(height: 5),
                    Text("잘못된 사진",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                          fontWeight: FontWeight.w500,
                          fontSize: 15
                      ),
                    )
                  ],
                ),
                Column(
                  mainAxisSize: MainAxisSize.min,
                  children: const [
                    Image(
                      image: AssetImage('assets/good-photo.jpg'),
                      width: 80,
                    ),
                    SizedBox(height: 5),
                    Text("좋은 사진",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                          fontWeight: FontWeight.w500,
                          fontSize: 15
                      ),
                    )
                  ],
                )
              ],
            ),
          ],
        ),
        actions: <Widget>[
          TextButton(
            onPressed: () async {
              var image = await ImagePicker.platform.getImage(
                  source: ImageSource.camera,
              );
              // File file = await ImagePicker.pickImage(source: ImageSource.camera);
              Navigator.pop(context, image);
            },
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: const [
                Icon(
                  Icons.camera_alt,
                  color: Colors.black,
                ),
                SizedBox(
                  width: 5,
                ),
                Text('카메라로 촬영하기',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                      fontWeight: FontWeight.w600,
                      color: Colors.black,
                      fontSize: 17
                  ),
                ),
              ],
            ),
          ),
          TextButton(
            onPressed: () async {
              var image = await ImagePicker.platform.getImage(
                  source: ImageSource.gallery,
              );
              // File file = await ImagePicker.pickImage(source: ImageSource.gallery);
              Navigator.pop(context, image);
            },
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: const [
                Icon(
                  Icons.photo_camera_back,
                  color: Colors.black,
                ),
                SizedBox(
                  width: 5,
                ),
                Text('앨범에서 가져오기',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                      fontWeight: FontWeight.w600,
                      color: Colors.black,
                      fontSize: 17
                  ),
                ),
              ],
            ),
          ),
        ] //backgroundColor: Colors.green,
      );
    },
  );
}

Text waringText(text) {
  return Text(text,
    textAlign: TextAlign.center,
    style: TextStyle(
        color: palette.black,
        fontWeight: FontWeight.w500,
        fontSize: 17
    ),
  );
}