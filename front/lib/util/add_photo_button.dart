import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

class AddPhotoButtonWidget extends StatefulWidget {

  const AddPhotoButtonWidget({
    Key? key,
    @required this.text,
    this.updateBool,
  }) : super(key: key);

  final text;
  final updateBool;

  @override
  AddPhotoButton createState() => AddPhotoButton();
}

class AddPhotoButton extends State<AddPhotoButtonWidget>{
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
                setState((){
                  widget.updateBool(widget.text);
                });
              },
            ),
            Text("${widget.text}면 등록하기",
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