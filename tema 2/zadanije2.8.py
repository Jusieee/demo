# -*- coding: utf-8 -*-

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

secret_message[3] = secret_message[3][::-1]

secret_message[4] = secret_message[4][::-1]

print(secret_message[0][3], secret_message[1][9:13], secret_message[2][5:15:2], secret_message[3][-13:-7],
      secret_message[4][-21:-16])


