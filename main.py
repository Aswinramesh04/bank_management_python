import streamlit as st
from bank_account import BankAccount

#session_state
if 'accounts' not in st.session_state:
    st.session_state['accounts'] = {}



def create_account():
    name = st.text_input("Enter your name:")
    account_number = st.number_input("Enter your account number:")

    if name and account_number:
        if account_number not in st.session_state['accounts']:
            st.session_state['accounts'][account_number] = BankAccount(name, account_number)
            st.success("Account created Successfully.")
        else:
            st.error("Account already exists.")

def select_account():
    account_options = list(st.session_state['accounts'].keys())
    if account_options:
        selected_account_number = st.selectbox("Select your account:",account_options)
        return st.session_state['accounts'][selected_account_number]
    else:
        st.warning("No account found.")
        return None


def main():
    st.title("My Bank")
    menu = ["Create Account", "Manage Account"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create Account":
        create_account()

    elif choice == "Manage Account":
        selected_account = select_account()
        if selected_account:
            st.subheader(f"Welcome, {selected_account.name}!!!!!")
            services = st.selectbox("Select Services:", ["Deposit", "Withdraw", "Check Balance"])

            if services == "Deposit":
                deposit_amount = st.number_input("Enter amount to deposit:")
                if deposit_amount > 0:
                    st.write(selected_account.deposit(deposit_amount))

            elif services == "Withdraw":
                withdraw_amount = st.number_input("Enter amount to withdraw:")
                if withdraw_amount > 0:
                    st.write(selected_account.withdraw(withdraw_amount))

            elif services == "Check Balance":
                st.write(selected_account.check_balance())


if __name__ == "__main__":
    main()