import 'package:flutter/material.dart';
import 'package:front/screens/result_screen_widget.dart';
import 'package:front/util/palette.dart' as palette;

import '../widgets/button/add_photo_button.dart';
import '../util/permission.dart';

class MainScreenWidget extends StatefulWidget{
  const MainScreenWidget({Key? key}) : super(key: key);

  @override
  MainScreen createState()=> MainScreen();
}

class MainScreen extends State<MainScreenWidget> {
  bool front = false;
  bool back = false;

  @override
  void initState() {
    // TODO: implement initState
    requestCameraPermission();
    requestPhotosPermission();
    super.initState();
  }


  @override
  Widget build(BuildContext context) {
    return SizedBox(
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
                    fontSize: 25,
                    fontWeight: FontWeight.bold
                ),
              ),
              SizedBox(
                height: 10,
              ),
              // TODO: 사진 추가하면, 추가한 사진이 Container에 들어가도록
              front ? Container(
                width: 200,
                height: 200,
                color: palette.gray
              ) : AddPhotoButtonWidget(text: "앞", updateBool: updateBool),
              SizedBox(
                height: 10,
              ),
              // TODO: 사진 추가하면, 추가한 사진이 Container에 들어가도록
              back ? Container(
                  width: 200,
                  height: 200,
                  color: palette.gray
              ) : AddPhotoButtonWidget(text: "뒷", updateBool: updateBool),
              SizedBox(
                height: 20,
              ),
              SizedBox(
                width: 200,
                height: 45,
                child: ElevatedButton(
                  child: const Text('검색하기',
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 20,
                          fontWeight: FontWeight.bold
                      )),
                  style: (front&&back) ?
                  ButtonStyle(backgroundColor: palette.darkBlueColor)
                      : ButtonStyle(backgroundColor: palette.grayColor),
                  onPressed: (front&&back) ? () {
                    goToResultPage(context);
                    setState((){
                      front = !front;
                      back = !back;
                    });
                  } : null,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void updateBool(String inputBool){
    setState((){
      if(inputBool == '앞')
      {
        front = !front;
      }
      else if(inputBool == '뒷')
      {
        back = !back;
      }
    });
  }

  void goToResultPage (context) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => ResultScreenWidget()),
    );
  }
}

