import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;
import 'package:flutter/services.dart';

import '../api/search_pill.dart';
import '../widgets/card/build_another_pill_card.dart';
import '../widgets/card/build_pill_info_card.dart';
import '../widgets/card/text_for_pill_info.dart';
import '../widgets/dialog/bulid_progress.dart';

class ResultScreenWidget extends StatefulWidget {
  final frontPhoto;
  final backPhoto;
  const ResultScreenWidget(this.frontPhoto, this.backPhoto);

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
                return buildProgress();
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
                              SizedBox(
                                height: 120,
                                child: Image.network(snapshot.data!.main.pillImg,
                                  fit: BoxFit.cover
                                ),
                              ),
                              const SizedBox(height: 8.0),
                              Card(
                                  elevation: 2.0,
                                  child: Padding(
                                    padding: const EdgeInsets.all(10.0),
                                    child: Column(
                                      children: [
                                        Padding(
                                          padding: const EdgeInsets.only(top: 5.0),
                                          child: Text(snapshot.data!.main.className.toString(),
                                            style: const TextStyle(
                                                fontWeight: FontWeight.bold,
                                                fontSize: 25),
                                          ),
                                        ),
                                        Container(
                                            margin: const EdgeInsets.only(left: 10, right: 10),
                                            width: double.infinity,
                                            child: Divider(color: palette.gray, thickness: 2.0)
                                        ),
                                        textForPillInfo("품목명", snapshot.data!.main.itemName.toString()),
                                        textForPillInfo("제조수입사", snapshot.data!.main.emtpName.toString())
                                      ],
                                    ),
                                  )
                              ),
                              Column(
                                  children: [
                                    (snapshot.data!.main.efficacy.toString().trim() != "")
                                        ? buildPillInfoCard(
                                          '효능효과',
                                          snapshot.data!.main.efficacy.toString()
                                    ):Container(),
                                    (snapshot.data!.main.dosage.toString().trim() != "")
                                        ? (
                                        (snapshot.data!.main.pictogramList.dosage != []) ?
                                        buildPillInfoPhotoCardWithString(
                                            '용법/용량',
                                            snapshot.data!.main.dosage.toString(),
                                            snapshot.data!.main.pictogramList.dosage)
                                            :buildPillInfoCard(
                                            '용법/용량',
                                            snapshot.data!.main.dosage.toString())
                                    ):Container(),
                                    (snapshot.data!.main.atpnWarnQesitm.toString().trim() != "")
                                        ? (
                                        (snapshot.data!.main.pictogramList.atpnWarnQesitm != []) ?
                                        buildPillInfoPhotoCardWithString(
                                            '사용전, 주의사항경고',
                                            snapshot.data!.main.atpnWarnQesitm.toString(),
                                            snapshot.data!.main.pictogramList.atpnWarnQesitm)
                                            :buildPillInfoCard(
                                            '사용전, 주의사항경고',
                                            snapshot.data!.main.atpnWarnQesitm.toString())
                                    ):Container(),
                                    (snapshot.data!.main.atpnQesitm.toString().trim() != "")
                                        ? (
                                        (snapshot.data!.main.pictogramList.atpnQesitm != []) ?
                                        buildPillInfoPhotoCardWithString(
                                            '사용시, 주의사항',
                                            snapshot.data!.main.atpnQesitm.toString(),
                                            snapshot.data!.main.pictogramList.atpnQesitm)
                                            :buildPillInfoCard(
                                            '사용시, 주의사항',
                                            snapshot.data!.main.atpnQesitm.toString())
                                    ):Container(),
                                    (snapshot.data!.main.intrcQesitm.toString().trim() != "")
                                        ? (
                                        (snapshot.data!.main.pictogramList.intrcQesitm != []) ?
                                        buildPillInfoPhotoCardWithString(
                                            '사용시, 주의해야 할 음식 및 약',
                                            snapshot.data!.main.intrcQesitm.toString(),
                                            snapshot.data!.main.pictogramList.intrcQesitm)
                                            :buildPillInfoCard(
                                            '사용시, 주의해야 할 음식 및 약',
                                            snapshot.data!.main.intrcQesitm.toString())
                                    ):Container(),
                                    (snapshot.data!.main.seQesitm.toString().trim() != "")
                                        ? (
                                        (snapshot.data!.main.pictogramList.seQesitm != []) ?
                                        buildPillInfoPhotoCardWithString(
                                            '부작용',
                                            snapshot.data!.main.seQesitm.toString(),
                                            snapshot.data!.main.pictogramList.seQesitm)
                                            :buildPillInfoCard(
                                            '부작용',
                                            snapshot.data!.main.seQesitm.toString())
                                    ):Container(),
                                    (snapshot.data!.main.depoditMetodQesirm.toString().trim() != "")
                                        ? (
                                        (snapshot.data!.main.pictogramList.depoditMetodQesirm != []) ?
                                        buildPillInfoPhotoCardWithString(
                                            '보관법',
                                            snapshot.data!.main.depoditMetodQesirm.toString(),
                                            snapshot.data!.main.pictogramList.depoditMetodQesirm)
                                            :buildPillInfoCard(
                                            '보관법',
                                            snapshot.data!.main.depoditMetodQesirm.toString())
                                    ):Container(),
                                  ]
                              ),
                              Container(
                                alignment: Alignment.bottomLeft,
                                padding: const EdgeInsets.only(
                                    left: 10.0, right: 10.0, top: 20.0, bottom: 5.0),
                                child: const Text("찾고 있는 약이 아닌가요? \n비슷한 약도 확인해보세요.",
                                  style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                      fontSize: 20),
                                ),
                              ),
                              Column(
                                children: snapshot.data!.others.map<Widget>(
                                        (data)=>BuildAnotherPillCard(
                                          context,
                                          data)
                                ).toList()
                              ),
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