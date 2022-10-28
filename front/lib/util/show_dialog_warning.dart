import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

import '../screens/result_screen_widget.dart';

ShowDialogWarning(BuildContext context) async {
  await showDialog(
    context: context,
    builder: (BuildContext context) {
      return  Center(
        child: SimpleDialog(
          title: Text('사진 등록 시 주의사항!',
            textAlign: TextAlign.center,
            style: TextStyle(
              color: palette.red,
              fontWeight: FontWeight.bold
            ),
          ),
          elevation: 10,
          children:[
            waringText("1. 밝은 조명 아래서 찍어주세요."),
            waringText("2. 알약이 전부 보이게 찍어주세요."),
            waringText("3. 깔끔한 배경에서 찍어주세요."),
            SizedBox(
              height: 20,
            ),
            waringText("*예시*"),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Column(
                  children: const [
                    Image(
                      image: AssetImage('assets/pill-icon-nobackground.png'),
                      width: 80,
                    ),
                    Text("잘못된 사진",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                          fontWeight: FontWeight.w400,
                          fontSize: 13
                      ),
                    )
                  ],
                ),
                Column(
                  children: const [
                    Image(
                      image: AssetImage('assets/pill-icon-nobackground.png'),
                      width: 80,
                    ),
                    Text("좋은 사진",
                      textAlign: TextAlign.center,
                      style: TextStyle(
                          fontWeight: FontWeight.w400,
                          fontSize: 13
                      ),
                    )
                  ],
                )
              ],
            ),
            SizedBox(
              height: 20,
            ),
            // 사진 삽입 선택 버튼
            Column(
              children: [
                SimpleDialogOption(
                  onPressed: () {
                    Navigator.pop(context);
                    goToResultPage(context);
                  },
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: const [
                      Icon(
                        Icons.camera_alt,
                      ),
                      SizedBox(
                        width: 5,
                      ),
                      Text('카메라로 촬영하기',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                            fontWeight: FontWeight.w600,
                            fontSize: 15
                        ),
                      ),
                    ],
                  ),
                ),
                SimpleDialogOption(
                  onPressed: () {
                    Navigator.pop(context);
                    goToResultPage(context);
                  },
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: const [
                      Icon(
                        Icons.photo_camera_back,
                      ),
                      SizedBox(
                        width: 5,
                      ),
                      Text('앨범에서 가져오기',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                            fontWeight: FontWeight.w600,
                            fontSize: 15
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ],
          //backgroundColor: Colors.green,
        ),
      );
    },
  );
}

void goToResultPage (context) {
  Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => ResultScreenWidget()),
  );
}

Text waringText(text) {
  return Text(text,
    textAlign: TextAlign.center,
    style: TextStyle(
        color: palette.black,
        fontWeight: FontWeight.w600,
        fontSize: 15
    ),
  );
}