class Pictogram {
  final List<String> dosage;
  final List<String> atpnWarnQesitm;
  final List<String> atpnQesitm;
  final List<String> seQesitm;
  final List<String> depoditMetodQesirm;
  final List<String> intrcQesitm;

  Pictogram({
    required this.dosage,
    required this.atpnWarnQesitm,
    required this.atpnQesitm,
    required this.seQesitm,
    required this.depoditMetodQesirm,
    required this.intrcQesitm
  });


  factory Pictogram.fromJson(Map<String, dynamic> pictogramMap){
    // List<String> infoImg = new List<String>.from(infoImgFromJson);
    List<String> dosage = List<String>.from(pictogramMap['Dosage']);
    List<String> atpnWarnQesitm = List<String>.from(pictogramMap['AtpnWarnQesitm']);
    List<String> atpnQesitm = List<String>.from(pictogramMap['AtpnQesitm']);
    List<String> intrcQesitm = List<String>.from(pictogramMap['IntrcQesitm']);
    List<String> seQesitm = List<String>.from(pictogramMap['SeQesitm']);
    List<String> depoditMetodQesirm = List<String>.from(pictogramMap['DepositMethodQesitm']);

    return Pictogram(
      dosage: dosage,
      atpnWarnQesitm: atpnWarnQesitm,
      atpnQesitm: atpnQesitm,
      intrcQesitm: intrcQesitm,
      seQesitm: seQesitm,
      depoditMetodQesirm: depoditMetodQesirm,
    );
  }

}