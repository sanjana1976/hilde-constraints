{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNE13shHTCrGA+0y35KBGqn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sanjana1976/-hilde-dynamic-constraints/blob/master/api_key_managment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GfH71N8dyrNF",
        "outputId": "94f9be53-b17f-4a1f-c0dd-e0abe2eb9d05"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "API key provided via command line.\n",
            "✅ API key set successfully!\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "import sys\n",
        "\n",
        "def setup_api_key():\n",
        "    \"\"\"\n",
        "    Set up OpenAI API key with multiple fallback options.\n",
        "    Returns True if successful, False otherwise.\n",
        "    \"\"\"\n",
        "    api_key = None\n",
        "\n",
        "    # Option 1: Check command-line argument\n",
        "    if len(sys.argv) > 1:\n",
        "        api_key = sys.argv[1]\n",
        "        print(\"API key provided via command line.\")\n",
        "\n",
        "    # Option 2: Check environment variable\n",
        "    elif os.environ.get(\"OPENAI_API_KEY\"):\n",
        "        api_key = os.environ.get(\"OPENAI_API_KEY\")\n",
        "        print(\"API key found in environment variables.\")\n",
        "\n",
        "    # Option 3: Interactive prompt\n",
        "    else:\n",
        "        api_key = input(\"Please enter your OpenAI API key: \")\n",
        "\n",
        "    # Store it as an environment variable\n",
        "    if api_key:\n",
        "        os.environ[\"OPENAI_API_KEY\"] = api_key\n",
        "        print(\"✅ API key set successfully!\")\n",
        "        return True\n",
        "    else:\n",
        "        print(\"❌ API key not set.\")\n",
        "        return False\n",
        "\n",
        "def get_api_key():\n",
        "    \"\"\"\n",
        "    Get the current API key from environment variables.\n",
        "    Returns the key if found, None otherwise.\n",
        "    \"\"\"\n",
        "    return os.environ.get(\"OPENAI_API_KEY\")\n",
        "\n",
        "def verify_api_key():\n",
        "    \"\"\"\n",
        "    Verify that the API key is set and accessible.\n",
        "    Returns True if valid, False otherwise.\n",
        "    \"\"\"\n",
        "    key = get_api_key()\n",
        "    if key:\n",
        "        print(f\"✅ API key is set (length: {len(key)} characters)\")\n",
        "        return True\n",
        "    else:\n",
        "        print(\"❌ No API key found\")\n",
        "        return False\n",
        "\n",
        "# Auto-setup when imported\n",
        "if __name__ == \"__main__\":\n",
        "    setup_api_key()\n",
        "else:\n",
        "    # If imported as module, just verify\n",
        "    verify_api_key()"
      ]
    }
  ]
}