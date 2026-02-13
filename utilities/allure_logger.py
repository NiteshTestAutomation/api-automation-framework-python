import allure

def allure_log_response(response):
    allure.attach(
        str(response.status_code),
        name="Status Code",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        str(response.headers),
        name="Response Headers",
        attachment_type=allure.attachment_type.TEXT
    )

    allure.attach(
        response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )


