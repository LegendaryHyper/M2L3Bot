# Görev 2 - İhtiyacınız olan her şeyi içe aktarın

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        # Görev 3 - Satır içi klavyeyi oluşturmak için bir yöntem oluşturun
        return buttons

# Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Kediler onları kimse görmediğinde ne yapar?", 1, "Uyurlar", "Mem yazarlar"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
   Question("Kediler hangi kitapları okumayı sever?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: Günde 18 saat nasıl uyunur","Sahibinizden 5 dakika erken uyumanın 101 yolu", "İnsan yönetimi rehberi")
]

