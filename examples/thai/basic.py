from pylatex import Document, Section, Subsection, Command, Package
from pylatex.utils import italic, NoEscape

if __name__ == '__main__':
    doc = Document('basic', inputenc = None, lmodern = False, fontenc = None, textcomp = None)

    packages = [
        Package('babel', options = ['english', 'thai']),
        Package('inputenc', options = 'utf8enc'),
        Package('fontspec'),
        ]
    #doc.packages.append(Package('babel', options = ['english', 'thai']))
    doc.packages.append(Package('fontspec'))
    doc.packages.append(Package('xunicode'))
    doc.packages.append(Package('xltxtra'))
    doc.append(NoEscape(r'\XeTeXlinebreaklocale "th_TH"'))
    doc.append(NoEscape(r'\XeTeXlinebreakskip = 0pt plus 1pt'))
    doc.append(NoEscape(r'\defaultfontfeatures{Scale=1.23}'))
    doc.append(NoEscape(r'\setmainfont[Mapping=tex-text]{TH SarabunPSK}'))

    text=r'Thai sentence is in quotes: "สวัสดี". Can you see thai?'
    text2=r"""
        11 รัฐมนตรีรอดจากศึกซักฟอกครั้งที่ 4 ไปตามความคาดหมาย ด้วยเสียงส่วนใหญ่ของที่ประสภาผู้แทนราษฎร โดยมี ส.ส. พรรคเศรษฐกิจไทย และ ส.ส. "กลุ่ม 16" ร่วมโหวตไว้วางใจ พล.อ. ประยุทธ์ จันทร์โอชา ด้วย
        ปัจจุบันมีพรรคการเมืองที่มีที่นั่งในสภาทั้งสิ้น 25 พรรค แบ่งเป็น พรรคร่วมฝ่ายค้าน 7 พรรค รวม 208 เสียง (ยังไม่หัก ส.ส. "งูเห่า" หรือ "ฝากเลี้ยง" ที่ชื่อยังอยู่ในสังกัดพรรคฝ่ายค้าน แต่มีพฤติกรรมการโหวตสนับสนุนรัฐบาล) พรรคเศรษฐกิจไทย ซึ่งประกาศตัวเป็น "ฝ่ายค้านอิสระ" 16 เสียง ส่วนที่เหลืออีก 253 เสียง มาจาก 17 พรรคร่วมรัฐบาล
        ในการผ่านญัตติไว้วางใจหรือไม่ไว้วางใจรัฐมนตรี ต้องอาศัยเสียงมากกว่ากึ่งหนึ่งของจำนวน ส.ส. ทั้งหมดเท่าที่มีอยู่ของสภา หรือ 239 เสียง จาก ส.ส. ที่ปฏิบัติหน้าที่ได้ 477 คน
        บีบีซีไทยตรวจสอบเอกสารผลการลงมติญัตติขอเปิดอภิปรายไม่ไว้วางใจฯ วันนี้ (23 ก.ค.) จัดทำโดยสำนักรายงานการประชุมและชวเลข เพื่อตามหาว่าคะแนนเสียงที่นายกฯ และ 10 รัฐมนตรีได้รับในสัดส่วนแตกต่างกันไป มีที่มาที่ไปอย่างไร ก่อนสรุปรูปแบบการลงคะแนนของบรรดาผู้แทนราษฎร โดยจำแนกเป็นรายพรรคได้ ดังนี้
        1. พรรคการเมืองที่สมาชิกลงมติอย่างเป็นเอกภาพ ไม่มี ส.ส. แตกแถวแม้แต่คนเดียวไม่ว่าจะลงมติให้รัฐมนตรีรายใด มีทั้งสิ้น 4 พรรครัฐบาล ประกอบด้วย พรรคภูมิใจไทย (ภท.) 62 คน, พรรคพลังท้องถิ่นไท (พทท.) 5 คน, พรรครวมพลัง (ร.พ.) 5 คน และพรรคชาติพัฒนา (ชพน.) 4 คน ทั้งนี้ไม่นับกรณีรัฐมนตรีที่ถูกอภิปรายซึ่งลงมติงดออกเสียงให้ตัวเอง
        2. พรรคเพื่อไทย (พท.) แกนนำพรรคฝ่ายค้าน มี ส.ส. 7 คน จากทั้งหมด 132 คน ไม่ได้ลงมติตามทิศทางของพรรค แต่เลือกโหวตไว้วางใจให้รัฐมนตรีสังกัด ภท. 2 คน และเลือกโหวตงดออกเสียงให้แก่นายกฯ และรัฐมนตรีรายอื่น ๆ
        สำหรับ 7 นักการเมืองกลุ่มนี้ ประกอบด้วย นายจักรพรรดิ ไชยสาส์น ส.ส.อุดรธานี, นายจาตุรงค์ เพ็งนรพัฒน์ ส.ส.ศรีสะเกษ, นายธีระ ไตรสรณกุล ส.ส.ศรีสะเกษ, นายนิยม ช่างพินิจ ส.ส.พิษณุโลก, นางผ่องศรี แซ่จึง ส.ส.ศรีสะเกษ, นายวุฒิชัย กิตติธเนศวร ส.ส.นครนายก และนายสุชาติ ภิญโญ ส.ส.นครราชสีมา ซึ่งแม้ชื่อยังอยู่ในสังกัดของ พท. โดยนิตินัย แต่โดยพฤตินัยที่แสดงออกผ่านการลงมตินัดสำคัญ ๆ ไม่ได้เป็นไปตามแนวทางของพรรคมานานแล้ว
        นอกจากนี้ยังมีอีก 1 คนคือ นายนพคุณ รัฐผไท ส.ส.เชียงใหม่ ที่ไม่ปรากฏว่ามีการลงคะแนนให้รัฐมนตรีรายใดเลย ซึ่งมีความหมายว่า ไม่ลงมติ/ลาประชุม/ขาดประชุม ทราบในภายหลังว่าแจ้งลาป่วยเพราะติดโรคโควิด-19
        3. พรรคก้าวไกล (ก.ก.) ซึ่งเป็นพรรคอันดับสองของฝ่ายค้าน มี ส.ส. 5 คน จากทั้งหมด 51 คน ไม่ได้ลงมติตามทิศทางของพรรค แต่มีทั้งการข้ามขั้วไปลงมติไว้วางใจให้แก่รัฐมนตรีบางคน และงดออกเสียงให้รัฐมนตรีบางคน
        สำหรับ 5 นักการเมืองกลุ่มนี้ ประกอบด้วย นายเกษมสันต์ มีทิพย์ ส.ส.บัญชีรายชื่อ, นายคารม พลพรกลาง ส.ส.บัญชีรายชื่อ, นายพีรเดช คำสมุทร ส.ส.เชียงราย, นายเอกภพ เพียรวิเศษ ส.ส.เชียงราย และนายขวัญเลิศ พานิชมาท ส.ส.ชลบุรี โดยเป็นกลุ่มคนหน้าเดิมที่มักลงมติต่างไปจากแนวของพรรคสีส้ม
        นอกจากนี้ยังมี 2 ส.ส.ที่ไม่ปรากฏผลคะแนนเป็นบางช่วงคือ นายวุฒินันท์ บุญชู ส.ส.สมุทรปราการ ไม่ปรากฏผลคะแนนระหว่างลงมติไว้วางใจ/ไม่ไว้วางใจ พล.อ. ประยุทธ์ จันทร์โอชา และ น.ส.วรรณวรี ตะล่อมสิน ส.ส.กทม. ไม่ปรากฏผลคะแนนระหว่างลงมติไว้วางใจ/ไม่ไว้วางใจนายสันติ พร้อมพัฒน์ รมช.คลัง
    """
    doc.append(text)
    doc.append(text2.encode('utf-8').decode('utf-8'))
    doc.generate_pdf(clean_tex=False, compiler='xelatex')
    doc.generate_tex()