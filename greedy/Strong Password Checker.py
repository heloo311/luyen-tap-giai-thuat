
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        pass

    def find_repqet_index(self,password):
        partitions= []
        previous_split=0
        for i in range(1,len(password)):
            if password[i-1] != password[i]:
                partitions.append(password[previous_split:i])
                previous_split=i
        partitions.append(password[previous_split:len(password)])
        print(partitions)

        max_length = max(len(i) for i in partitions)
        if max_length<3:
            return -1

    def has_upper_lower_and_digit(self,password):
        has_upper = any(i.isupper() for i in password)
        has_lower = any(i.islower() for i in password)
        has_digit = any(i.isdigit() for i in password)

        if has_lower and has_upper and has_digit:
            return True
        return False

    def is_strongpassword(self,password):
        pass

a= Solution()
a.find_repqet_index('aaaabb')
