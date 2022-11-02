import 'dart:io';
import 'package:flutter/material.dart';
import 'package:front/screens/result_screen_widget.dart';
import 'package:image_picker/image_picker.dart';
import 'package:front/util/palette.dart' as palette;

import '../widgets/button/add_photo_button.dart';
import '../util/permission.dart';

class MainScreenWidget extends StatefulWidget{
  const MainScreenWidget({Key? key}) : super(key: key);

  @override
  MainScreen createState()=> MainScreen();
}

class MainScreen extends State<MainScreenWidget> {
  XFile? _pickedFrontPhoto;
  XFile? _pickedBackPhoto;

  final String _logoImage = 'assets/pill-icon-nobackground.png';

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
                image: AssetImage(_logoImage),
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
                    fontWeight: FontWeight.w500
                ),
              ),
              SizedBox(
                height: 10,
              ),
              // TODO: 사진 추가하면, 추가한 사진이 Container에 들어가도록 (server)
              (_pickedFrontPhoto != null) ? Container(
                width: 200,
                height: 200,
                // color: palette.gray,
                decoration: BoxDecoration(
                  image: DecorationImage(
                      image: FileImage(File(_pickedFrontPhoto!.path)),
                      fit: BoxFit.cover
                  ),
                ),
              ) : AddPhotoButtonWidget(text: "앞", updatePhoto: updatePhoto),
              SizedBox(
                height: 10,
              ),
              // TODO: 사진 추가하면, 추가한 사진이 Container에 들어가도록 (server)
              (_pickedBackPhoto != null) ? Container(
                  width: 200,
                  height: 200,
                  decoration: BoxDecoration(
                    image: DecorationImage(
                        image: FileImage(File(_pickedBackPhoto!.path)),
                        fit: BoxFit.cover
                  ),
                ),
              ) : AddPhotoButtonWidget(text: "뒷", updatePhoto: updatePhoto),
              SizedBox(
                height: 20,
              ),
              SizedBox(
                width: 200,
                height: 45,
                child: ElevatedButton(
                  // TODO: (server) 사진 보내서 데이터 받기
                  child: const Text('검색하기',
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 20,
                          fontWeight: FontWeight.bold
                      )),
                  style: ((_pickedFrontPhoto != null) && (_pickedBackPhoto != null)) ?
                  ButtonStyle(backgroundColor: palette.darkBlueColor)
                      : ButtonStyle(backgroundColor: palette.grayColor),
                  onPressed: ((_pickedFrontPhoto != null) && (_pickedBackPhoto != null)) ? () {
                    goToResultPage(context);
                    setState((){
                      _pickedFrontPhoto = null;
                      _pickedBackPhoto = null;
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

  void updatePhoto(String inputBool, XFile photo){
    setState((){
      if(inputBool == '앞')
      {
        _pickedFrontPhoto = photo;
      }
      else if(inputBool == '뒷')
      {
        _pickedBackPhoto = photo;
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

