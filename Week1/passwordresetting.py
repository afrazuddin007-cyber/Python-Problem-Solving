from prompt_toolkit.key_binding.bindings.named_commands import uppercase_word

np=str(input("Enter a new password: "))
cp=str(input("Confirm password: "))
if np==cp:
    print("Password is correct")

else:
    if np.casefold() == cp.casefold():
        print("Check for the cases instead")
    else:
        print("Password does not match")