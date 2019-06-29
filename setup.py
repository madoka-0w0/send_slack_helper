import setuptools

setuptools.setup(
    name="send_slack_helper",
    version="1.0",
    author="madoka takagi",
    author_email="mad106.t@gmail.com",
    description="send some message for slack url (incoming webhook).",
    long_description="send some message for slack url (incoming webhook).",
    long_description_content_type="text/markdown",
    url="https://xmadoka.hatenablog.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.0a3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['injector', "boto3", "slackweb"],
    python_requires='>=3',
)
