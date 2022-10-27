import 'package:flutter/material.dart';
import 'package:front/screens/result_screen_widget.dart';
import 'package:front/util/palette.dart' as palette;

import '../util/add_photo_button.dart';

class MainScreenWidget extends StatefulWidget{
  const MainScreenWidget({Key? key}) : super(key: key);
  MainScreen createState()=> MainScreen();
}

class MainScreen extends State<MainScreenWidget> {
  final bool front = false;
  final bool back = false;

  @override
  Widget build(BuildContext context) {
    return Container(
        width: double.infinity,
        height: double.infinity,
        child: Scaffold(
          body: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Image(
                  image: AssetImage('assets/pill-icon-nobackground.png'),
                  width: 70,
                ),
                SizedBox(
                  height: 10,
                ),
                Text(
                  '사진으로 알약을 검색해보세요!',
                  style: TextStyle(
                    color: palette.black,
                    fontSize: 20,
                    fontWeight: FontWeight.bold
                  ),
                ),
                SizedBox(
                  height: 30,
                ),
                AddPhotoButton(text: "앞", updateBool: updateBool, side: front),
                SizedBox(
                  height: 20,
                ),
                AddPhotoButton(text: "뒷", updateBool: updateBool, side: back),
                SizedBox(
                  height: 30,
                ),
                SizedBox(
                  width: 200,
                  height: 40,
                  child: ElevatedButton(
                    child: const Text('검색하기',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 17,
                        fontWeight: FontWeight.bold
                    )),
                    style: (front&&back) ?
                    ButtonStyle(backgroundColor: palette.darkBlueColor)
                    : ButtonStyle(backgroundColor: palette.grayColor),
                    onPressed: (front&&back) ? () {
                      goToResultPage();
                    } : null,
                  ),
                ),
              ],
            ),
          ),
        )
    );
  }

  void updateBool(bool inputBool){
    setState((){
      inputBool = !inputBool;
    });
  }

  void goToResultPage () {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => ResultScreenWidget()),
    );
  }
}