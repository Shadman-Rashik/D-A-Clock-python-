{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOgOlEPgPUBxi8INwySCUth"
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
      "cell_type": "code",
      "source": [
        "import os\n",
        "import time\n",
        "from datetime import datetime\n",
        "\n",
        "def clear_screen():\n",
        "    os.system('cls' if os.name == 'nt' else 'clear')\n",
        "\n",
        "def display_watch():\n",
        "    while True:\n",
        "        clear_screen()\n",
        "        now = datetime.now()\n",
        "        current_time = now.strftime(\"%H:%M:%S\")\n",
        "        print(\"Current Time:\", current_time)\n",
        "        time.sleep(1)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    display_watch()\n"
      ],
      "metadata": {
        "id": "uuH-e665qTPB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}