
for f in *.svg; do
    s=${f##*/};
    convert -background none -density 2000 -resize 50x50 -bordercolor none -border 5 $f ${s%.*}.png;
done

cp battery-missing-symbolic.png battery-missing.png
cp battery-caution-symbolic.png battery-caution.png
cp battery-low-symbolic.png battery-low.png
cp battery-empty-symbolic.png battery-missing.png
cp battery-good-symbolic.png battery-good.png
cp battery-full-symbolic.png battery-full.png
cp battery-caution-charging-symbolic.png battery-caution-charging.png
cp battery-low-charging-symbolic.png battery-low-charging.png
cp battery-good-charging-symbolic.png battery-good-charging.png
cp battery-full-charging-symbolic.png battery-full-charging.png
cp battery-full-charged-symbolic.png battery-full-charged.png

cp network-idle.png network-online.png
cp network-receive.png network-acquiring.png

cp audio-volume-high-panel.png audio-volume-high.png
cp audio-volume-medium-panel.png audio-volume-medium.png
cp audio-volume-low-panel.png audio-volume-low.png
cp audio-volume-muted-panel.png audio-volume-muted.png
