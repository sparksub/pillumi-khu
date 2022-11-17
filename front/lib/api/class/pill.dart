import 'package:front/api/class/pictogram.dart';

class Pill {
  final String itemName;
  final String emtpName;
  final String className;
  final String efficacy;
  final String dosage;
  final String atpnWarnQesitm;
  final String atpnQesitm;
  final String seQesitm;
  final String depoditMetodQesirm;
  final String pillImg;
  final String intrcQesitm;

  final Pictogram pictogramList;

  Pill({
    required this.itemName,
    required this.emtpName,
    required this.className,
    required this.efficacy,
    required this.dosage,
    required this.atpnWarnQesitm,
    required this.atpnQesitm,
    required this.seQesitm,
    required this.depoditMetodQesirm,
    required this.pillImg,
    required this.intrcQesitm,
    required this.pictogramList
  });

  factory Pill.fromJson(Map<String, dynamic> pillMap){
    return Pill(
        itemName: pillMap['ITEM_NAME'],
        emtpName: pillMap['ENTP_NAME'],
        className: pillMap['CLASS_NAME'],
        efficacy: pillMap['Efficacy'],
        dosage: pillMap['Dosage'],
        atpnWarnQesitm: pillMap['AtpnWarnQesitm'],
        atpnQesitm: pillMap['AtpnQesitm'],
        intrcQesitm: pillMap["IntrcQesitm"],
        seQesitm: pillMap['SeQesitm'],
        depoditMetodQesirm: pillMap['DepositMethodQesitm'],
        pillImg: pillMap['PillImg'],
        pictogramList: Pictogram.fromJson(pillMap['PictogramList'])
    );
  }
}