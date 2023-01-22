wget https://raw.githubusercontent.com/L1ghtDream/raport/cdn/dependencies.py
python3 dependencies.py
git clone $RAPORT_URL raport
cp process.data raport/process.data
cd raport
git add *
git checkout -b "${{ env.ARTIFACT }}/${{ env.VERSION }}"
git config --global user.email "bot@voinearadu.com"
git config --global user.name "Radu Voinea [bot]"
git commit -m "${{ env.ARTIFACT }}/${{ env.VERSION }}"
git remote set-url origin https://L1ghtDream:${{ secrets.PERSONAL_TOKEN }}@github.com/L1ghtDream/raport
git push --set-upstream origin ${{ env.ARTIFACT }}/${{ env.VERSION }}