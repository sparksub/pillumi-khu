import 'package:flutter/material.dart';
import 'package:front/util/palette.dart' as palette;

import '../widgets/card/build_pill_info_card.dart';
import '../widgets/card/text_for_pill_info.dart';

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
              child: Column(
                children: [
                  SizedBox(
                    height: 120,
                    child: Image.network(widget.pill.pillImg,
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
                              child: Text(widget.pill.className.toString(),
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
                            textForPillInfo("품목명", widget.pill.itemName.toString()),
                            textForPillInfo("제조수입사", widget.pill.emtpName.toString())
                          ],
                        ),
                      )
                  ),
                  Column(
                      children: [
                        (widget.pill.efficacy.toString().trim() != "")
                            ? buildPillInfoCard(
                            '효능효과',
                            widget.pill.efficacy.toString()
                        ):Container(),
                        (widget.pill.dosage.toString().trim() != "")
                            ? (
                            (widget.pill.pictogramList.dosage != []) ?
                            buildPillInfoPhotoCardWithString(
                                '용법/용량',
                                widget.pill.dosage.toString(),
                                widget.pill.pictogramList.dosage)
                                :buildPillInfoCard(
                                '용법/용량',
                                widget.pill.dosage.toString())
                        ):Container(),
                        (widget.pill.atpnWarnQesitm.toString().trim() != "")
                            ? (
                            (widget.pill.pictogramList.atpnWarnQesitm != []) ?
                            buildPillInfoPhotoCardWithString(
                                '사용전, 주의사항경고',
                                widget.pill.atpnWarnQesitm.toString(),
                                widget.pill.pictogramList.atpnWarnQesitm)
                                :buildPillInfoCard(
                                '사용전, 주의사항경고',
                                widget.pill.atpnWarnQesitm.toString())
                        ):Container(),
                        (widget.pill.atpnQesitm.toString().trim() != "")
                            ? (
                            (widget.pill.pictogramList.atpnQesitm != []) ?
                            buildPillInfoPhotoCardWithString(
                                '사용시, 주의사항',
                                widget.pill.atpnQesitm.toString(),
                                widget.pill.pictogramList.atpnQesitm)
                                :buildPillInfoCard(
                                '사용시, 주의사항',
                                widget.pill.atpnQesitm.toString())
                        ):Container(),
                        (widget.pill.intrcQesitm.toString().trim() != "")
                            ? (
                            (widget.pill.pictogramList.intrcQesitm != []) ?
                            buildPillInfoPhotoCardWithString(
                                '사용시, 주의해야 할 음식 및 약',
                                widget.pill.intrcQesitm.toString(),
                                widget.pill.pictogramList.intrcQesitm)
                                :buildPillInfoCard(
                                '사용시, 주의해야 할 음식 및 약',
                                widget.pill.intrcQesitm.toString())
                        ):Container(),
                        (widget.pill.seQesitm.toString().trim() != "")
                            ? (
                            (widget.pill.pictogramList.seQesitm != []) ?
                            buildPillInfoPhotoCardWithString(
                                '부작용',
                                widget.pill.seQesitm.toString(),
                                widget.pill.pictogramList.seQesitm)
                                :buildPillInfoCard(
                                '부작용',
                                widget.pill.seQesitm.toString())
                        ):Container(),
                        (widget.pill.depoditMetodQesirm.toString().trim() != "")
                            ? (
                            (widget.pill.pictogramList.depoditMetodQesirm != []) ?
                            buildPillInfoPhotoCardWithString(
                                '보관법',
                                widget.pill.depoditMetodQesirm.toString(),
                                widget.pill.pictogramList.depoditMetodQesirm)
                                :buildPillInfoCard(
                                '보관법',
                                widget.pill.depoditMetodQesirm.toString())
                        ):Container(),
                      ]
                  ),
                ],
              )
          ),
        ),
      ),
    );
  }
}
