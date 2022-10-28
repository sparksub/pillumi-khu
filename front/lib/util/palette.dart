import 'package:flutter/material.dart';
import 'create_material_color.dart';

MaterialColor red = createMaterialColor(Color(0xFFed1b24));
MaterialColor darkBlue = createMaterialColor(Color(0xFF23408e));
MaterialColor blue = createMaterialColor(Color(0xFF385399));
MaterialColor gray = createMaterialColor(Color(0xFFcccccc));
MaterialColor white = createMaterialColor(Color(0xFFffffff));
MaterialColor black = createMaterialColor(Color(0xFF000000));

MaterialStateProperty<Color?> redColor = MaterialStateProperty.all(Color(0xFFed1b24));
MaterialStateProperty<Color?> darkBlueColor = MaterialStateProperty.all(Color(0xFF23408e));
MaterialStateProperty<Color?> blueColor = MaterialStateProperty.all(Color(0xFF385399));
MaterialStateProperty<Color?> grayColor = MaterialStateProperty.all(Color(0xFFcccccc));
MaterialStateProperty<Color?> whiteColor = MaterialStateProperty.all(Color(0xFFffffff));
MaterialStateProperty<Color?> blackColor = MaterialStateProperty.all(Color(0xFF000000));