import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

class AddPhotoButton extends StatelessWidget {

  const AddPhotoButton({
    Key? key,
    @required this.text,
    this.updateBool,
    this.side,
  }) : super(key: key);

  final text;
  final updateBool;
  final side;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 200,
      height: 200,
      color: palette.gray,
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton(
              icon: Icon(
                Icons.add_a_photo,
              ),
              iconSize: 100,
              onPressed: (){
                updateBool(side);
              },
            ),
            Text("$text면 등록하기",
                style: const TextStyle(
                    fontSize: 17,
                    fontWeight: FontWeight.w500
                ))
          ],
        ),
      ),
    );
  }
}