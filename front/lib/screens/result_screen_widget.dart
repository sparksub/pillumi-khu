import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

import '../api/search_pill.dart';
import '../widgets/card/build_another_pill_card.dart';
import '../widgets/card/build_pill_info_card.dart';
import '../widgets/card/text_for_pill_info.dart';

class ResultScreenWidget extends StatefulWidget {
  final Future<Pill> resultPill;
  const ResultScreenWidget(this.resultPill);

  @override
  ResultScreen createState()=> ResultScreen();
}
class ResultScreen extends State<ResultScreenWidget> {
  String pillTitle = "약";
  String _pillImage = "assets/pill-icon-nobackground.png";
  String _pillEfficacy = "감기로 인한 발열 및 동통(통증), 두통, 신경통, 근육통, 월경통, 염좌통(삔 통증)";
  String _pillDosage = "만 12세 이상 소아 및 성인: 1회 1~2정씩 1일 3-4회 (4-6시간 마다) 필요시 복용한다. 1일 최대 4그램 (8정)을 초과하여 복용하지 않는다. 이 약은 가능한 최단기간동안 최소 유효용량으로 복용한다.";
  List<dynamic> _pillInfoImage = ["assets/sample_eat_info1.jpeg", "assets/sample_eat_info2.jpeg"];


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('검색결과'),
      ),
      body: Center(
        child: FutureBuilder<Pill>(
          future: widget.resultPill,
          builder: (BuildContext context, AsyncSnapshot snapshot){
            if(snapshot.hasData == false)
              {
                return Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text('검색 중입니다.',
                      style: TextStyle(fontSize: 20),
                    ),
                    SizedBox(height: 20.0,),
                    CircularProgressIndicator(
                      valueColor: AlwaysStoppedAnimation<Color>(palette.blue),
                    ),
                  ],
                );
              }
            else if (snapshot.hasError)
              {
                return Padding(
                  padding: const EdgeInsets.all(8.0),

                  child: Text(
                    'Error: ${snapshot.error}', // 에러명을 텍스트에 뿌려줌
                    style: TextStyle(fontSize: 15),
                  ),
                );
              }
            else{
              return SingleChildScrollView(
                scrollDirection: Axis.vertical,
                child: Container(
                    padding: const EdgeInsets.all(10),
                    child: Column(
                      children: [
                        // TODO: 검색된 알약 이미지 보여주기
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Image(
                              image: AssetImage(_pillImage),
                              width: 150,
                            ),
                            Image(
                              image: AssetImage(_pillImage),
                              width: 150,
                            ),
                          ],
                        ),
                        const SizedBox(height: 8.0),
                        // 알약에 대한 기본 정보
                        // TODO: 알약 정보 보여주는 method 연결
                        Card(
                            elevation: 2.0,
                            child: Padding(
                              padding: const EdgeInsets.all(10.0),
                              child: Column(
                                children: [
                                  Padding(
                                    padding: const EdgeInsets.only(top: 5.0),
                                    child: Text(snapshot.data!.className.toString(),
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
                                  textForPillInfo("품목명", snapshot.data!.itemName.toString()),
                                  textForPillInfo("제조수입사", snapshot.data!.emtpName.toString())
                                ],
                              ),
                            )
                        ),
                        buildPillInfoCard("효능효과", snapshot.data!.efficacy.toString()),
                        buildPillInfoCard("용법/용량", snapshot.data!.dosage.toString()),
                        buildPillInfoPhotoCard("복약정보", snapshot.data!.infoImg),
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
                        BuildAnotherPillCard(
                            "기타의 소화기관용약",
                            "가나모티정",
                            "assets/sample1.jpeg"),
                        BuildAnotherPillCard(
                            "비타민C 및 P제",
                            "국제아스코르빈산정",
                            "assets/sample2.jpeg"),
                      ],
                    )
                ),
              );
            }
          }
        ),
      ),
    );
  }
  //
  // Future _future() async {
  //   await Future.delayed(Duration(seconds: 5)); // 5초를 강제적으로 딜레이 시킨다.
  //   print(widget.resultPill);
  //   return '성공!'; // 5초 후 '짜잔!' 리턴
  // }
}