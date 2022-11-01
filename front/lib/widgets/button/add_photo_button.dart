import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;
import 'package:front/widgets/dialog/show_dialog_warning.dart';

class AddPhotoButtonWidget extends StatefulWidget {

  const AddPhotoButtonWidget({
    Key? key,
    @required this.text,
    this.updatePhoto,
  }) : super(key: key);

  final text;
  final updatePhoto;

  @override
  AddPhotoButton createState() => AddPhotoButton();
}

class AddPhotoButton extends State<AddPhotoButtonWidget>{
  var _photo;
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
              onPressed: () async {
                _photo = await ShowDialogWarning(context);
                setState((){
                  widget.updatePhoto(widget.text, _photo);
                });
              },
            ),
            Text("${widget.text}면 등록하기",
                style: const TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.w600
                ))
          ],
        ),
      ),
    );
  }
}