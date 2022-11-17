import 'package:flutter/material.dart';
import 'package:front/widgets/view/build_main_pill.dart';

class SimilarScreenWidget extends StatefulWidget {
  final pill;
  const SimilarScreenWidget(this.pill, {Key? key}) : super(key: key);

  @override
  State<SimilarScreenWidget> createState() => SimilarScreen();
}

class SimilarScreen extends State<SimilarScreenWidget> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('비슷한 알약'),
      ),
      body: Center(
        child: SingleChildScrollView(
          scrollDirection: Axis.vertical,
          child: Container(
              padding: const EdgeInsets.all(10),
              child: BuildMainPill(widget.pill)
          ),
        ),
      ),
    );
  }
}
