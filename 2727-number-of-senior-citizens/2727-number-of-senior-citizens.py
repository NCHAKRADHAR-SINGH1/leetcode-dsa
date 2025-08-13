class Solution(object):
    def countSeniors(self, details):
        count = 0
        dici = {'phone_number': 0, 'gender': 0, 'age': 0, 'seat_alloted': 0}
        for i in range(len(details)):
            person_details = details[i]
            n = len(person_details)
            dici['phone_number'] = person_details[:11]
            dici['gender'] = person_details[10:11]
            dici['age'] = person_details[11:13]
            dici['seat_alloted'] = person_details[13:n]
            
            # Convert age to int before comparing
            if int(dici['age']) > 60:
                count += 1
        return count

        