import 'package:flutter/material.dart';

import '../../api/class/pill.dart';
import '../card/build_pill_info_card.dart';
import '../card/text_for_pill_info.dart';

import 'package:front/util/palette.dart' as palette;

Column BuildMainPill(Pill mainPill) {
  return Column(
    children: [
      SizedBox(
        height: 120,
        child: Image.network(mainPill.pillImg,
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
                  child: Text(mainPill.className.toString(),
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
                textForPillInfo("품목명", mainPill.itemName.toString()),
                textForPillInfo("제조수입사", mainPill.emtpName.toString())
              ],
            ),
          )
      ),
      Column(
          children: [
            (mainPill.efficacy.toString().trim() != "")
                ? buildPillInfoCard(
                '효능효과',
                mainPill.efficacy.toString()
            ):Container(),
            (mainPill.dosage.toString().trim() != "")
                ? (
                (mainPill.pictogramList.dosage != []) ?
                buildPillInfoPhotoCardWithText(
                    '용법/용량',
                    mainPill.dosage.toString(),
                    mainPill.pictogramList.dosage)
                    :buildPillInfoCard(
                    '용법/용량',
                    mainPill.dosage.toString())
            ):Container(),
            (mainPill.atpnWarnQesitm.toString().trim() != "")
                ? (
                (mainPill.pictogramList.atpnWarnQesitm != []) ?
                buildPillInfoPhotoCardWithText(
                    '사용전, 주의사항경고',
                    mainPill.atpnWarnQesitm.toString(),
                    mainPill.pictogramList.atpnWarnQesitm)
                    :buildPillInfoCard(
                    '사용전, 주의사항경고',
                    mainPill.atpnWarnQesitm.toString())
            ):Container(),
            (mainPill.atpnQesitm.toString().trim() != "")
                ? (
                (mainPill.pictogramList.atpnQesitm != []) ?
                buildPillInfoPhotoCardWithText(
                    '사용시, 주의사항',
                    mainPill.atpnQesitm.toString(),
                    mainPill.pictogramList.atpnQesitm)
                    :buildPillInfoCard(
                    '사용시, 주의사항',
                    mainPill.atpnQesitm.toString())
            ):Container(),
            (mainPill.intrcQesitm.toString().trim() != "")
                ? (
                (mainPill.pictogramList.intrcQesitm != []) ?
                buildPillInfoPhotoCardWithText(
                    '사용시, 주의해야 할 음식 및 약',
                    mainPill.intrcQesitm.toString(),
                    mainPill.pictogramList.intrcQesitm)
                    :buildPillInfoCard(
                    '사용시, 주의해야 할 음식 및 약',
                    mainPill.intrcQesitm.toString())
            ):Container(),
            (mainPill.seQesitm.toString().trim() != "")
                ? (
                (mainPill.pictogramList.seQesitm != []) ?
                buildPillInfoPhotoCardWithText(
                    '부작용',
                    mainPill.seQesitm.toString(),
                    mainPill.pictogramList.seQesitm)
                    :buildPillInfoCard(
                    '부작용',
                    mainPill.seQesitm.toString())
            ):Container(),
            (mainPill.depoditMetodQesirm.toString().trim() != "")
                ? (
                (mainPill.pictogramList.depoditMetodQesirm != []) ?
                buildPillInfoPhotoCardWithText(
                    '보관법',
                    mainPill.depoditMetodQesirm.toString(),
                    mainPill.pictogramList.depoditMetodQesirm)
                    :buildPillInfoCard(
                    '보관법',
                    mainPill.depoditMetodQesirm.toString())
            ):Container(),
          ]
      ),
    ],
  );
}