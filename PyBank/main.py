{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'../Instructions/PyBank/Resources/budget_data.csv'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "csv_path = os.path.join(\"../Instructions/PyBank/Resources/budget_data.csv\")\n",
    "csv_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "\n",
      "------------------------\n",
      "\n",
      "Total Months: 86\n",
      "\n",
      "Total: $38382578\n",
      "\n",
      "Average Change: $446309.05\n",
      "\n",
      "Greatest Increase in Profits: Feb-2012 ($1170593)\n",
      "\n",
      "Greatest Decrease in Profits: Sep-2013 ($-1196225)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "totalMonths = 0\n",
    "month = []\n",
    "totalrev = 0\n",
    "rev = 0\n",
    "prerev = 0\n",
    "deltarev = 0\n",
    "deltarevList = []\n",
    "\n",
    "\n",
    "with open(csv_path,'r') as csv_file:\n",
    "\n",
    "    csv_reader = csv.reader(csv_file)\n",
    "    next(csv_reader)\n",
    "    \n",
    "    for row in csv_reader:\n",
    "        month.append(row[0])\n",
    "        deltarevList.append(int(row[1]))\n",
    "        \n",
    "totalMonths = len(month)\n",
    "        \n",
    "inc = deltarevList[0]\n",
    "dec = deltarevList[0]\n",
    "\n",
    "\n",
    "for row in range(len(deltarevList)):\n",
    "    if deltarevList[row] <= dec:\n",
    "        dec = deltarevList[row]\n",
    "        decMonth = month[row]\n",
    "    if deltarevList[row] >= inc:\n",
    "        inc = deltarevList[row]\n",
    "        incMonth = month[row]\n",
    "    totalrev = totalrev + deltarevList[row]\n",
    "    \n",
    "avgDelta = round(totalrev/totalMonths, 2)\n",
    "\n",
    "dest = os.path.join(\"../Instructions/PyBank/Resources/budget_data.txt\")\n",
    "\n",
    "print(\"Financial Analysis\" + \"\\n\")\n",
    "print(\"------------------------\" + \"\\n\")\n",
    "print(\"Total Months: \" + str(totalMonths) + \"\\n\")\n",
    "print(\"Total: $\" + str(totalrev) + \"\\n\")\n",
    "print(\"Average Change: $\" + str(avgDelta) + \"\\n\")\n",
    "print(\"Greatest Increase in Profits: \" + incMonth + \" ($\" + str(inc) + \")\"+ \"\\n\")\n",
    "print(\"Greatest Decrease in Profits: \" + decMonth + \" ($\" + str(dec) + \")\"+ \"\\n\")\n",
    "\n",
    "with open(dest, 'w') as writetxt:\n",
    "    writetxt.writelines(\"Financial Analysis\" + \"\\n\")\n",
    "    writetxt.writelines(\"------------------------\" + \"\\n\")\n",
    "    writetxt.writelines(\"Total Months: \" + str(totalMonths) + \"\\n\")\n",
    "    writetxt.writelines(\"Total: $\" + str(totalrev) + \"\\n\")\n",
    "    writetxt.writelines(\"Average Change: $\" + str(avgDelta) + \"\\n\")\n",
    "    writetxt.writelines(\"Greatest Increase in Profits: \" + incMonth + \" ($\" + str(inc) + \")\"+ \"\\n\")\n",
    "    writetxt.writelines(\"Greatest Decrease in Profits: \" + decMonth + \" ($\" + str(dec) + \")\"+ \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'writetext' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-102-6d5b26ba14f1>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mwritetext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'writetext' is not defined"
     ]
    }
   ],
   "source": [
    "writetext"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "86\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "446309.05"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Feb-2012'"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Sep-2013'"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
