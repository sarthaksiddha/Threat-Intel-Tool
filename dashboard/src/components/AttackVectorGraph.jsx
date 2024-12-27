import React from 'react';
import { ResponsiveSankey } from '@nivo/sankey';

const AttackVectorGraph = ({ data }) => (
  <div className="h-96">
    <ResponsiveSankey
      data={data}
      margin={{ top: 40, right: 160, bottom: 40, left: 50 }}
      align="justify"
      colors={{ scheme: 'category10' }}
      nodeOpacity={1}
      nodeHoverOthersOpacity={0.35}
      nodeThickness={18}
      nodeSpacing={24}
      nodeBorderWidth={0}
      nodeBorderColor={{ theme: 'background' }}
      linkOpacity={0.5}
      linkHoverOthersOpacity={0.1}
      linkContract={3}
      enableLinkGradient={true}
      labelPosition="outside"
      labelOrientation="horizontal"
      labelPadding={16}
      legends={[{
        anchor: 'bottom-right',
        direction: 'column',
        translateX: 130,
        itemWidth: 100,
        itemHeight: 14,
        itemDirection: 'right-to-left',
        itemsSpacing: 2,
        symbolSize: 14
      }]}
    />
  </div>
);

export default AttackVectorGraph;