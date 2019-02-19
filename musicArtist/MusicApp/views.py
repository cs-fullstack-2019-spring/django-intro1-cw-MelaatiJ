from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Start with the music route. ")


def music(request):
    return HttpResponse("Shaggy, brunomars, sade")


def brunomars(request):
    return HttpResponse("Peter Gene Hernandez (born October 8, 1985), known as Bruno Mars, is an American singer,"
                        " songwriter, multi-instrumentalist, record producer, and dancer. He is known for his stage"
                        " performances, retro showmanship and for performing in a wide range of musical styles including"
                        " R&B,funk, pop, soul, reggae, hip hop, and rock. Mars is accompanied by his band, The Hooligans"
                        "who play a variety of instruments such as electric guitar, bass, piano, keyboards, drums and"
                        " horns, and also serve as backup singers and dancers.")


def shaggy(request):
    return HttpResponse("Orville Richard Burrell CD (born October 22, 1968), better known by his stage name Shaggy, "
                        "is a Jamaican musician, singer, DJ and United States Marine who fought in the Persian Gulf War"
                        ". He is best known for his hit singles ""Oh Carolina," "Boombastic," "It Wasn't Me""and""Angel"
                ". He took his stage name from the character Shaggy, from the popular children's TV show Scooby-Doo.")

def sade(request):
    return HttpResponse("Helen Folasade Adu, CBE (Yoruba: Fọláṣadé Adú [fɔ̄láʃādé ādú]; born 16 January 1959), known"
                        " professionally as Sade Adu or simply Sade (/ʃɑːˈdeɪ/ shah-DAY), is a British Nigerian singer"
                        ", songwriter, and actress, known as the lead singer of her self-titled band.Born in Ibadan, "
                        "Nigeria and brought up in Essex, England, Sade gained modest recognition as a fashion designer"
                        " and part-time model, prior to joining the band Pride in the early 1980s. After gaining "
                        "attention as a performer, she formed the band Sade, and secured a recording contract with Epic"
                        " Records in 1983. The band then released the album Diamond Life a year later, which became one"
                        " of the best selling albums of the era, and the best-selling debut ever by a British female"
                        " vocalist. It also gained widespread critical acclaim and is largely considered one of the best "
                        "albums of all time. In July 1985, Sade was among the performers at the Live Aid charity concert"
                        " at Wembley Stadium.")