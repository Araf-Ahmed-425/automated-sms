from twilio.rest import Client
import random

# =======================================================
#  TWILIO ACCOUNT 1 (For Angkon)
# =======================================================
TWILIO1_SID = "AC0a607254a76f80f7a47039f6b571fca2"
TWILIO1_AUTH = "fc43abd3d86876e1c3c33612ee047796"
TWILIO1_FROM = "+16303497544"
TWILIO1_TO = "+8801925987071"   # Angkon's number


# =======================================================
#  TWILIO ACCOUNT 2 (For Rafi)
# =======================================================
TWILIO2_SID = "AC21867950d82cd96e137175beadd6fe74"
TWILIO2_AUTH = "55624fc8e79bb285d87f30f742ba81c9"
TWILIO2_FROM = "+19522420521"
TWILIO2_TO = "+8801912563397"  # Rafi's number



# =======================================================
# RANDOM MCQ PATTERN
# =======================================================
def generate_mcq_pattern():
    letters = ["A", "B", "C", "D", "E"]
    return "".join(random.sample(letters, 5))


# =======================================================
# BUILD RESULT MESSAGE
# =======================================================
def build_message(name, programme, subject, week,
                  written_get, written_total,
                  mcq_total, mcq_correct, mcq_incorrect):

    mcq_skip = mcq_total - (mcq_correct + mcq_incorrect)
    mcq_marks = mcq_correct - (mcq_incorrect * 0.25)

    total_get = written_get + mcq_marks
    total_total = written_total + mcq_total

    msg = (
        f"\n{name}'s Result\n"
        f"{programme} Daily MCQ and Written Exam {subject}-{week}\n"
        f"Written: {written_get}/{written_total}\n"
        f"MCQ: {mcq_marks}/{mcq_total}\n"
        f"Total: {total_get}/{total_total}\n"
        f"MCQ Cor-{mcq_correct} , Inc-{mcq_incorrect} , Skip-{mcq_skip}\n"
        f"1-5. {generate_mcq_pattern()}\n"
        f"6-10. {generate_mcq_pattern()}\n"
        f"11-15. {generate_mcq_pattern()}\n"
        f"16-20. {generate_mcq_pattern()}"
    )

    return msg


# =======================================================
# SEND USING TWILIO ACCOUNT 1
# =======================================================
def send_twilio_1(message):
    client = Client(TWILIO1_SID, TWILIO1_AUTH)
    sms = client.messages.create(
        body=message,
        from_=TWILIO1_FROM,
        to=TWILIO1_TO
    )
    print("[TWILIO-1] Sent! SID:", sms.sid)


# =======================================================
# SEND USING TWILIO ACCOUNT 2
# =======================================================
def send_twilio_2(message):
    client = Client(TWILIO2_SID, TWILIO2_AUTH)
    sms = client.messages.create(
        body=message,
        from_=TWILIO2_FROM,
        to=TWILIO2_TO
    )
    print("[TWILIO-2] Sent! SID:", sms.sid)


# =======================================================
# MENU & EXECUTION
# =======================================================
print("Where do you want to send SMS?")
print("1. Angkon (Twilio Account #1)")
print("2. Rafi   (Twilio Account #2)")

choice = input("Enter 1 or 2: ")

msg1 = build_message(
    name="Angkon",
    programme="Versity-A Admission Programme",
    subject="M",
    week="09",
    written_get=2.5,
    written_total=2.5,
    mcq_total=20,
    mcq_correct=15,
    mcq_incorrect=3
)

msg2 = build_message(
    name="Rafi",
    programme="EAP",
    subject="C",
    week="09",
    written_get=8,
    written_total=10,
    mcq_total=20,
    mcq_correct=16,
    mcq_incorrect=2
)

if choice == "1":
    print("\nGenerated Message for Angkon:")
    print(msg1)
    print("\nSending...")
    send_twilio_1(msg1)

elif choice == "2":
    print("\nGenerated Message for Rafi:")
    print(msg2)   # FIXED!
    print("\nSending...")
    send_twilio_2(msg2)

else:
    print("Invalid choice!")