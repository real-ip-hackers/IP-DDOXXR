from colorama import Fore
import ddoser
import doxxxxxxxx
import ratdeployer
print(Fore.RED+ "IP" + Fore.GREEN + "-DDOXXR v1.0")
print(Fore.BLUE)
a = input("Do you want to use DDOSER (1), DOXXXER (2) or RAT DEPLOYER (3)? ")
match(a):
    case "1":
        ddoser.ddoser()
    case "2":
        doxxxxxxxx.doxxer()
    case "3":
        ratdeployer.ratInterface()
    case default:
        print("invalid tool")