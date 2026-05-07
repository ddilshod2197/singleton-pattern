class DesignPattern:
    def __init__(self):
        self.patterns = {
            "Singleton": "Singleton - bir nechta obyekt yaratishni cheklaydigan dizayn modeli",
            "Factory": "Factory - obyekt yaratish uchun muayyan uslubni aniqlashga yordam beruvchi dizayn modeli",
            "Observer": "Observer - obyekt o'zgarishlarini boshqa obyektlarga yoyishga yordam beruvchi dizayn modeli",
            "Strategy": "Strategy - obyektning xatti-harakatini o'zgartirishga yordam beruvchi dizayn modeli",
            "Template": "Template - obyektning xatti-harakatini belgilashga yordam beruvchi dizayn modeli",
        }

    def get_pattern(self, name):
        return self.patterns.get(name)

    def list_patterns(self):
        return list(self.patterns.keys())

design_pattern = DesignPattern()
print(design_pattern.get_pattern("Singleton"))
print(design_pattern.list_patterns())
