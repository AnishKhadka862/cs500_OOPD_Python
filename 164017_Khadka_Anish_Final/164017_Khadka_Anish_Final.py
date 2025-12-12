from __future__ import annotations
from state_machine import (
    State,
    Event,
    acts_as_state_machine,
    before,
    after,
    InvalidStateTransition
)


@acts_as_state_machine
class HouseBuyingProcess:
    Browsing = State(initial=True)
    Viewing = State()
    Offering = State()
    Negotiating = State()
    UnderContract = State()
    preApproval = State()
    Inspection = State()
    Closing = State()
    Completed = State()

    start_viewing = Event(from_states=(Browsing,), to_state=Viewing)
    place_offer = Event(from_states=(Viewing,), to_state=Offering)
    negotiate = Event(from_states=(Offering,), to_state=Negotiating)
    accept_offer = Event(from_states=(Negotiating,), to_state=UnderContract)

    start_preapproval = Event(from_states=(UnderContract,), to_state=preApproval)
    loan_approved = Event(from_states=(preApproval,), to_state=Inspection)
    loan_rejected = Event(from_states=(preApproval,), to_state=Browsing)

    inspection = Event(from_states=(Inspection,), to_state=Inspection)
    close_deal = Event(from_states=(Inspection,), to_state=Closing)
    finalize = Event(from_states=(Closing,), to_state=Completed)
    offer_again = Event(from_states=(Negotiating,), to_state=Offering)

    restart = Event(from_states=(Completed,), to_state=Browsing)

    cancel = Event(
        from_states=(Viewing, Offering, Negotiating, UnderContract, preApproval, Inspection),
        to_state=Browsing
    )

    def __init__(self, agency: "RealEstate") -> None:
        self.__agency = agency

    @before("start_viewing")
    def before_viewing(self) -> None:
        self.__agency.prepare_viewing()

    @after("start_viewing")
    def after_viewing(self) -> None:
        print("You are now viewing a house.")

    @before("place_offer")
    def before_offer(self) -> None:
        self.__agency.collect_offer_details()

    @after("place_offer")
    def after_offer(self) -> None:
        print("Your offer has been submitted.")

    @after("negotiate")
    def after_negotiate(self) -> None:
        print("Negotiation started with seller.")

    @after("accept_offer")
    def after_accept(self) -> None:
        print("Your offer was accepted. Under contract.")

    @after("start_preapproval")
    def after_pre_approval(self) -> None:
        print("Loan pre-approval process has started.")

    @after("loan_approved")
    def after_loan_approved(self) -> None:
        print("Loan approved. Proceeding to inspection.")

    @after("loan_rejected")
    def after_loan_rejected(self) -> None:
        print("Loan rejected. Returning to browsing.")

    @after("inspection")
    def after_inspection(self) -> None:
        print("Inspection in progress.")

    @after("close_deal")
    def after_close(self) -> None:
        print("Closing paperwork is being prepared.")

    @after("finalize")
    def after_finalize(self) -> None:
        print("Congratulations! The house is yours.")

    @after("offer_again")
    def after_offer_again(self) -> None:
        print("Submitting a new offer after negotiation.")

    @after("cancel")
    def after_cancel(self) -> None:
        print("Process cancelled. Returning to browsing.")

    @after("restart")
    def after_restart(self) -> None:
        print("System reset. Ready to browse houses again.")


class RealEstate:
    def __init__(self) -> None:
        self.__process = HouseBuyingProcess(self)

    def prepare_viewing(self) -> None:
        print("Scheduling a house viewing...")

    def collect_offer_details(self) -> None:
        print("Collecting offer details from buyer...")

    def start_viewing(self): self.__process.start_viewing()
    def place_offer(self): self.__process.place_offer()
    def negotiate(self): self.__process.negotiate()
    def accept_offer(self): self.__process.accept_offer()
    def start_preapproval(self): self.__process.start_preapproval()
    def loan_approved(self): self.__process.loan_approved()
    def loan_rejected(self): self.__process.loan_rejected()
    def inspection(self): self.__process.inspection()
    def close_deal(self): self.__process.close_deal()
    def finalize(self): self.__process.finalize()
    def cancel(self): self.__process.cancel()
    def offer_again(self): self.__process.offer_again()
    def restart(self): self.__process.restart()
    def get_state(self):
        return self.__process.current_state


def show_menu() -> None:
    print()
    print("===== HOUSE BUYING MENU =====")
    print("1. Start Viewing")
    print("2. Place Offer")
    print("3. Negotiate")
    print("4. Accept Offer")
    print("5. Offer Again")
    print("6. Start Pre-Approval")
    print("7. Loan Approved")
    print("8. Loan Rejected")
    print("9. Inspection")
    print("10. Close Deal")
    print("11. Finalize Purchase")
    print("12. Cancel Process")
    print("13. Restart")
    print("14. Exit")


def main() -> None:
    agency = RealEstate()

    action_names = {
        1: "Start Viewing",
        2: "Place Offer",
        3: "Negotiate",
        4: "Accept Offer",
        5: "Offer Again",
        6: "Start Pre-Approval",
        7: "Loan Approved",
        8: "Loan Rejected",
        9: "Inspection",
        10: "Close Deal",
        11: "Finalize Purchase",
        12: "Cancel Process",
        13: "Restart",
        14: "Exit"
    }

    while True:
        show_menu()
        choice_text = input("Enter choice number: ")

        try:
            choice = int(choice_text)
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            if choice == 1:
                agency.start_viewing()
            elif choice == 2:
                agency.place_offer()
            elif choice == 3:
                agency.negotiate()
            elif choice == 4:
                agency.accept_offer()
            elif choice == 5:
                agency.offer_again()
            elif choice == 6:
                agency.start_preapproval()
            elif choice == 7:
                agency.loan_approved()
            elif choice == 8:
                agency.loan_rejected()
            elif choice == 9:
                agency.inspection()
            elif choice == 10:
                agency.close_deal()
            elif choice == 11:
                agency.finalize()
            elif choice == 12:
                agency.cancel()
            elif choice == 13:
                agency.restart()
            elif choice == 14:
                print("Exiting system.")
                break
            else:
                print("Invalid option.")
                continue

            action_name = action_names.get(choice, "Unknown Action")
            print(f"current state: {action_name}")

        except InvalidStateTransition:
            action_name = action_names.get(choice, "Unknown Action")
            print(f"Action '{action_name}' is not allowed when current state is '{agency.get_state()}'.")


if __name__ == "__main__":
    main()