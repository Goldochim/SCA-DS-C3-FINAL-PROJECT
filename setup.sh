mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"goldochim2@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = 0.0.0.0\n\
" > ~/.streamlit/config.toml
