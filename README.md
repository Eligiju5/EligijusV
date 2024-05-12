# EligijusV
<h2>Kursinis darbas. Birthday reminder</h2>
Kursinio darbo tikslas yra įtvirtinti ir parodyti žinias, įgytas semestro metu. Ši programa vartotojui parodo kurių asmenų, įrašytų į failą, gimtadieniai yra ši diena. Paleidus programą, matome keturis pasirinkimus:

1. Paspaudus 1, galime pridėti gimtadienį, įrašydami jį į failą, visų pirma įrašomas vartotojo vardas, tuomet asmens, kurio gimimo datą norime pridėti, galiausiai data(formatas pateikiamas pačioje programoje). 
2. Paspaudus 2, galime pašalinti gimimo datą iš failo, užtenka pasirinkti vartotoją ir parašyti vardą asmens, kurio gimimo datą norime pašalinti.
3. Paspaudus 3 ir įrašius vartotojo varda, bus atspausdinami visi vardai asmenų, kurių gimtadieniai yra šiandien.
4. Paspaudus 4 programa išsijungia.

Ši programa atitinka reikalavimus, nes ji leidžia pridėti/pašalinti gimtadienius į/iš failo, atspausdinti priminimus gimtadienio dieną bei palaiko kelis vartotojus.
Taip pat naudojami:

<p>Polymorphism "print(f"It's {self.name}'s birthday today!")"</p>
</p>Abstraction "raise NotImplementedError("Subclasses must implement notify method")"</p>
</p>Inheritance "class BirthdayReminder(Reminder): "</p>
<p>Encapsulation "self.name = name </p>
</p>Singleton "cls._instance = super().__new__(cls)"</p>
</p>Factory Method "return BirthdayReminder(name, date)"</p>


Ši programa veikia taip, kaip ir turėtų veikti, tačiau nėra labai efektyvi, kiekvienam vartotojui reiktų gimtadienius rašyti po vieną, tai užtruktų tikrai nemažai laiko.
Didėjant priminimų ir vartotojų skaičiui, programos našumas gali pablogėti, ypač įkeliant ir išsaugant duomenis.
Duomenų vientisumas: gali būti sudėtinga užtikrinti, kad faile saugomi duomenys išliktų nuoseklūs ir tikslūs, ypač pridedant ar pašalinant priminimus.

Darydamas šį darbą supratau, kad išmokti naują programavimo kalbą buvo visai nesunku, Python šiuo metu yra mano geriausiai suprantama ir mėgstamiausia kalba. Tai, jog visa informacija, gauta paskaitų bei laboratornių darbų metu yra iš tiesų naudinga ir reikalinga, padeda gilinti žinias ir praktinius programavimo gebėjimus.

Ateityje būtų galima perdaryti programą taip, kad ji duomenis pildytų ar imtų iš duomenų bazės, tokiu būdu ji taptų naudingesnė bei efektyvesnė. Be to, įmanoma perdaryti programą taip, kad ji gimtadienio dieną, automatiškai atsiųstų tam tikram asmeniui pranešimą elektroniniu paštu arba žmogui, kurio tą dieną gimtadienis, palinkėjimą.
