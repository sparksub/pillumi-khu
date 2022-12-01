import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../api/class/pill_list.dart';
import '../api/search_pill.dart';
import '../widgets/dialog/bulid_progress.dart';
import '../widgets/view/build_main_pill.dart';
import '../widgets/view/build_other_pill.dart';

class ResultScreenWidget extends StatefulWidget {
  final frontPhoto;
  final backPhoto;
  const ResultScreenWidget(this.frontPhoto, this.backPhoto, {super.key});

  @override
  ResultScreen createState()=> ResultScreen();
}
class ResultScreen extends State<ResultScreenWidget> {
  var logData;

  @override
  void initState(){
    SystemChrome.setEnabledSystemUIMode(SystemUiMode.manual, overlays: SystemUiOverlay.values);
    logData = SearchPill(widget.frontPhoto, widget.backPhoto);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Center(
        child: FutureBuilder<PillList>(
            future: SearchPill(widget.frontPhoto, widget.backPhoto),
            builder: (BuildContext context, AsyncSnapshot snapshot){
              if(snapshot.hasData == false)
              {
                return Scaffold(
                    body: buildProgress()
                );
              }
              else if (snapshot.hasError)
              {
                return Padding(
                  padding: const EdgeInsets.all(8.0),

                  child: Text(
                    'Error: ${snapshot.error}', // 에러명을 텍스트에 뿌려줌
                    style: const TextStyle(fontSize: 15),
                  ),
                );
              }
              else if (snapshot.data!.main.itemName == 'NONE')
              {
                return Padding(
                  padding: const EdgeInsets.all(8.0),

                  child: Text(
                    '검색에 실패했습니다.', // 에러명을 텍스트에 뿌려줌
                    style: const TextStyle(fontSize: 15),
                  ),
                );
              }
              else
              {
                return Scaffold(
                  appBar: AppBar(
                    title: const Text('검색결과'),
                  ),
                  body: Center(
                    child: SingleChildScrollView(
                      scrollDirection: Axis.vertical,
                      child: Container(
                          padding: const EdgeInsets.all(10),
                          child: Column(
                            children: [
                              BuildMainPill(snapshot.data!.main),
                              BuildOtherPill(snapshot.data!.others, context),
                            ],
                          )
                      ),
                    ),
                  ),
                );
              }
            }
        ),
      ),
    );
  }


//

}