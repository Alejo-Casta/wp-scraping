from playwright.sync_api import sync_playwright

def send_message(contacto, mensaje):
    with sync_playwright() as p:
        browser = p.firefox.launch_persistent_context(user_data_dir="./data/session.json", slow_mo=500)
        page = browser.new_page()

        page.goto("https://web.whatsapp.com")
        page.wait_for_selector('[data-testid="chat-list-search"]')
        page.fill('[data-testid="chat-list-search"]', contacto)
        page.wait_for_selector(f'span[title="{contacto}"]')
        page.click(f'span[title="{contacto}"]')
        page.wait_for_selector('[data-testid="conversation-compose-box-input"]')
        page.fill('[data-testid="conversation-compose-box-input"]', mensaje)
        page.wait_for_selector('[data-testid="compose-btn-send"]')
        page.click('[data-testid="compose-btn-send"]')

        browser.close()


send_message("Amor", "Prueba exitosa de que soy el mejor!")
